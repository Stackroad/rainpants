import http.client, urllib
import pymongo
from pymongo import MongoClient
import datetime

# response.xpath('//*[@id="wpt_startpage_vtableWeather"]/div/table/tbody/tr[1]/td[3]/div[1]/div[1]/span[1]').extract()
# response.xpath('//div[contains(@class, "name")]/h1/text()')[0].extract()
#response.css('div.content').extract()
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    page_url = "https://www.klart.se/se/%C3%B6sterg%C3%B6tlands-l%C3%A4n/v%C3%A4der-link%C3%B6ping/"

    def start_requests(self):
        urls = [
            "https://www.klart.se/se/%C3%B6sterg%C3%B6tlands-l%C3%A4n/v%C3%A4der-link%C3%B6ping/"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #page = response.url.split("/")[-2]
        #filename = "quotes-%s.html" % page
        # with open(filename, "wb") as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)

        print(response.css('title::text').extract())
        msgRaw = response.xpath('normalize-space(//*[@id="day-1"]/article/div[1]/div[4]/div/p/text())')[0].extract()

        msgSplit = msgRaw.split(' ')
        msgSplit = msgSplit[0]
        msg = float(msgSplit.replace(',','.'))



        client = MongoClient()
        client = MongoClient('localhost', 27017)
        client = MongoClient('mongodb://localhost:27017/')
        db = client['mydb']
        collection = db.test_collection
        collection = db['test-collection']

        post = {"day": datetime.datetime.utcnow(),
            "rain": '6,1 mm'}
        posts = db.posts
        post_id = posts.insert_one(post).inserted_id
        print(post_id)


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
