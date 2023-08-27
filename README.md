Calendar Web-scraper 
--------------------------
Creator: Mohammed Sakib
Description: a Web-Scraper built using python libraries—BeautifulSoup, ics, and datetime—to create an .ics file with important dates and events to import into google calendar.

Motivation: My motivation for this project was to simplify the process of transferring important event and dates from the college website to my google calendar. There were over 75 important dates and evnets on the college website, excluding the dates the were not relevant to my schedule, and entering all these dates manually would become tedious. So, I decided to figure out a way to automate the process. 

What it does: I figured I could do accomplish this task by trying to create an .ics file from the webpage using a web-scraper. The university website also provided a simplified html page with dates that would be easier to print so I decided to take advantage of this and use this page to scrape the data more easily (HTML page included in college_calendar.html). So after finding the two useful libraries, beautifulsoup4 and ics, I developed a program that could take the information from webpage, storing it in a dictlist, and convert the information into an .ics file.

To use this web-scraper, I load and open an html file which I then read using the beautifulsoup4 library methods. The program iterate through the information, storing it in a dictlist in python. Then, it takes each dictionary in the list and appends each dictionary into an collegecal.ics file as events.

