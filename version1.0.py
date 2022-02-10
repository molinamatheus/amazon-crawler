!pip install furl
!pip install selenium
!apt-get update # to upgrade ubuntu to currectly run apt install
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin
#this script is responsible for to introduce all systems and libraries that will be used

import bs4
from bs4 import BeautifulSoup
import sys
sys.path.insert(0,'/usr/lib/chromium-browser')
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriververWait
from lxml.html.soupparser import fromstring
#this script is responsible for getting the library selenium and beatfulsoup

path=https://www.amazon.com/s?bbn=16225009011&rh=n%3A2811119011&dc&qid=1644500557&rnid=16225009011&ref=lp_16225009011_nr_n_3
#this is the variable reffering to the website

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
#Selenium WebDriver is an automated testing framework used for website validation
#The ChromeOptions class was introduced in the latest/updated version of Selenium.
#It is useful to make changes in the Chrome browser

browser=webdriver.Chrome('chromedriver',options=chrome_options)
browser.get(path)
soup=BeautifulSoup(browser.page_source,'html.parser')
#this moment the script open dev function in browser (type inspect)

_searchresult='div[id="mainResults"]>ul>li'
#<li> (Lista dos Itens de um elemento HTML) é usado para representar um item que faz parte de uma lista.
# Este item deve estar contido em uma lista desordenada ( <ul> )
job_elements=soup.select(_searchresult)

len(job_elements)
#len return the number of elements in any list
_title='h2'
x=job_elements[0]
t=x.select(_title)[0]
title=t.get_text()

_price=x.select('span[class="a-size-base a-color-price a-text-bold"]')

valuePrice = None

for _price in _price:
    #The for loop allows you to execute a block of code over and over again until a condition is true.
    # The in operator checks if the operand to its left is contained in the list to its right.
    valuePricePresent = float(_price.get_text().replace('$',''))
    if valuePrice==None
        valuePrice=valuePricePresent
    else:
        if valuePricePresent<valuePrice
            valuePrice=valuePricePresent
price=str(valuePrice)
print('iten:'+title)
print('price:'+price)
#return all results in string (text)

_nextpg=soup.select('a[id="pagnNextlink"]')[0]
path=_nextpg.get('href')
#this script is responsible to introduce next page in browser


