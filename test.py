import http.client, urllib


# response.xpath('//*[@id="wpt_startpage_vtableWeather"]/div/table/tbody/tr[1]/td[3]/div[1]/div[1]/span[1]').extract()
# response.xpath('//div[contains(@class, "name")]/h1/text()')[0].extract()
#response.css('div.content').extract()
import scrapy



class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):

        urls = [
            "https://www.klart.se/se/östergötlands-län/väder-linköping/"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = "quotes-%s.html" % page
        with open(filename, "wb") as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

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



# if __name__ == '__main__':
#     push()


    # user_key = 'u8xx2b59ao8nvuancemrx8p4tegx9g'
    # for user_key in user_keys:
    #     try:
    #         conn = http.client.HTTPSConnection("api.pushover.net:443")
    #         conn.request("POST", "/1/messages.json",
    #             urlencode({
    #                 "token": API_TOKEN ,
    #                 "user": user_key,
    #                 "message":  msg,
    #                 "url": page_url,
    #                 "url_title": 'Dagens hästlista',
    #             }), { "Content-type": "application/x-www-form-urlencoded" })
    #         conn.getresponse()
    #     except:
    #         print('Failed!')
    #     else:
    #         print('Success!')
