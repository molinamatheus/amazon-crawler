from bs4 import BeautifulSoup

from selenium import webdriver

# this script is responsible for getting the library selenium and beatfulsoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver

path = 'https://www.amazon.com/s?bbn=16225009011&rh=n%3A2811119011&dc&qid=1644500557&rnid=16225009011&ref=lp_16225009011_nr_n_3'
# this is the variable reffering to the website

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
# Selenium WebDriver is an automated testing framework used for website validation
# The ChromeOptions class was introduced in the latest/updated version of Selenium.
# It is useful to make changes in the Chrome browser
service = Service('.\chromedriver')

browser: WebDriver = webdriver.Chrome('.\chromedriver')
while path is not None:
    browser.get(path)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    # print('soup', soup)
    # this moment the script open dev function in browser (type inspect)

    _searchresult = 'div[class="s-main-slot s-result-list s-search-results sg-row"]>div'
    # <li> (Lista dos Itens de um elemento HTML) é usado para representar um item que faz parte de uma lista.
    # Este item deve estar contido em uma lista desordenada ( <ul> )
    job_elements = soup.select(_searchresult)
    print(len(job_elements))
    # len return the number of elements in any list
    _title = 'div[class="a-section a-spacing-none a-spacing-top-small s-title-instructions-style"] > h2'
    for x in job_elements:
        _t = x.select(_title)
        if _t is None or len(_t) == 0:
            pass
        else:
            t = _t[0]
            title = t.get_text()
            print('title: ', title)

            _pricelist = x.select('span[class="a-price"] > span[class="a-offscreen"]')
            print('_pricelist:', _pricelist)
            valuePrice = None

            for _price in _pricelist:
                # The for loop allows you to execute a block of code over and over again until a condition is true.
                # The in operator checks if the operand to its left is contained in the list to its right.
                valuePriceText = _price.get_text()
                print('valuePriceText', valuePriceText)
                valuePricePresent = float(valuePriceText.replace('$', ''))
                if valuePrice == None:
                    valuePrice = valuePricePresent
                else:
                    if valuePricePresent < valuePrice:
                        valuePrice = valuePricePresent
            price = str(valuePrice)
            print('iten:' + title)
            print('price:' + price)
            # return all results in string (text)

    _nextpg = soup.select(
        '#search > div.s-desktop-width-max.s-desktop-content.s-opposite-dir.sg-row > div.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div > span:nth-child(4) > div.s-main-slot.s-result-list.s-search-results.sg-row > div:nth-child(40) > div > div > span > a.s-pagination-item.s-pagination-next.s-pagination-button.s-pagination-separator')
    print(_nextpg)
    path = _nextpg[0].get('href')
    # this script is responsible to introduce next page in browser
