import http.client, urllib
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

import scrapy

#page_url = "https://www.smhi.se/q/Link%C3%B6ping/2694762#!,"
#page_url = "https://news.ycombinator.com/"
page_url = "https://www.klart.se/"
def push():

    print('Trying to push!')
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
      urllib.parse.urlencode({
        "token": "anho9ycivxnw86p774i9qsc2to78ym",
        "user": "u8xx2b59ao8nvuancemrx8p4tegx9g",
        "message": "hello world",
      }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()

def parse_page(url):
    print('Parsing page')
    req = Request(url)
    webpage = urlopen(req).read()
    # page = urlopen(url)
    soup = BeautifulSoup(webpage, 'html.parser')

    return soup

def main(page_url):
    soup = parse_page(page_url)


    test = soup.find(id='js-scroll')
    #test2 = test.find(class_='wpt_row')
    #test2 = test.find('div', class_='wpt_row')
    print(test)
    # for rain in soup.find_all('span'):
    #     header = rain.find('div', {'class': 'unit'}).get_text()
    #     print(header)
    #print(soup.prettify())
    # for rain in soup.find_all('div', {'id': 'wpt_startpage_vtableWeather'}):
    #     today = rain.find('div', {'class': 'value'}).get_text()
    #     print(today)

if __name__ == '__main__':
    #push()
    #soup = parse_page(page_url)
    main(page_url)
