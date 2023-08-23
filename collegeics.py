from bs4 import BeautifulSoup
from ics import Calendar, Event
import re
from datetime import datetime as dt


def main():
    write_ics(events_scraper("college_calendar.html"))

def events_scraper(html):
    with open(html, 'r') as file:
        content = file.read()

        soup = BeautifulSoup(content, 'lxml')
        event_tags = soup.find_all('li')
        eventslist = []

        for tag in event_tags:
            if not "(Half Term)" in tag.contents[3].contents[1].contents[1].text:
                eventdict = {}
                name = tag.contents[3].contents[1].contents[1].text.rstrip('.').replace('Full ', '').lstrip().replace(u'\xa0', u'')
                time = tag.contents[1].contents[1].text.strip()
                time2 = re.sub(r" (\d), ", lambda x: f" 0{x.group(1)}, ", time)
                time3 = re.sub(r" \d\d:\d\dpm", "", time2)
                time4 = re.sub(r"[A-Z][a-z][a-z], ", "", time3)
                eventdict["name"] = name
                eventdict["time"] = dt.strptime(time4, "%b %d, %Y").strftime("%Y-%m-%d")
                eventslist.append(eventdict)
        return eventslist

def write_ics(elist):
    cal = Calendar()
    for edict in elist:
        event = Event()
        event.name = edict["name"]
        event.begin = f'{edict["time"]} 00:00:00'
        event.make_all_day()
        cal.events.add(event)

    with open('collegecal.ics', 'w') as f:
        f.writelines(cal.serialize_iter())


if __name__ == "__main__":
    main()