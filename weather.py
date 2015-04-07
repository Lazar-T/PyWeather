import re
import urllib
from bs4 import BeautifulSoup


COLOR_RED = "\033[01;31m{0}\033[00m"
COLOR_BLUE = "\033[1;36m{0}\033[00m"
COLOR_WHITE = "\033[1;37m{0}\033[00m"


print """
This is small weather program that lets you enter your location and
then it prints out current temperature, and highest-lowest temperatures
in the next four days.
"""

location = raw_input('Enter where you live: ')
count = len(re.findall(r'\w+', location))

# if location has more than one word in it, add '+' between them
if count > 1:
    location.split(',')
    '+'.join(location)

page_url = 'http://thefuckingweather.com/?where=%s&unit=c' % location

page = urllib.urlopen(page_url)
soup = BeautifulSoup(page)


current_temp = soup.select('.temperature')[0].text

first_day_high = soup.select('.temperature')[1].text
second_day_high = soup.select('.temperature')[2].text
third_day_high = soup.select('.temperature')[3].text
fourth_day_high = soup.select('.temperature')[4].text

first_day_low = soup.select('.temperature')[5].text
second_day_low = soup.select('.temperature')[6].text
third_day_low = soup.select('.temperature')[7].text
fourth_day_low = soup.select('.temperature')[8].text


print COLOR_WHITE.format("\nCurrent temperature is: %sC") % current_temp


print COLOR_RED.format("""
In the next 4 days highest temperature are going to be:
------------------------
%s   %s   %s   %s
------------------------
""") % (first_day_high, second_day_high, third_day_high, fourth_day_high)


print COLOR_BLUE.format("""
In the next 4 days lowest temperature is going to be:
------------------------
%s   %s   %s   %s
------------------------
""") % (first_day_low, second_day_low, third_day_low, fourth_day_low)
