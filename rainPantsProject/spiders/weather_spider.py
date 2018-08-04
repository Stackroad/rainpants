import http.client, urllib
import pymongo
from pymongo import MongoClient
import datetime
import scrapy

class WeatherSpider(scrapy.Spider):
    name = "weather"
    page_url = "https://www.klart.se/se/hallands-l%C3%A4n/v%C3%A4der-varberg/"
    #page_url = "https://www.klart.se/se/%C3%B6sterg%C3%B6tlands-l%C3%A4n/v%C3%A4der-link%C3%B6ping/"

    def start_requests(self):
        urls = [
            "https://www.klart.se/se/hallands-l%C3%A4n/v%C3%A4der-varberg/"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response.css('title::text').extract())
        msgRaw = response.xpath('normalize-space(//*[@id="day-1"]/article/div[1]/div[4]/div/p/text())')[0].extract()

        msgSplit = msgRaw.split(' ')
        msgSplit = msgSplit[0]
        msg = float(msgSplit.replace(',','.'))

        client = MongoClient()
        client = MongoClient('localhost', 27017)
        client = MongoClient('mongodb://localhost:27017/')
        db = client['mydb']
        
        post = {"day": datetime.datetime.utcnow(),
            "rain": msg
            }
        posts = db.posts
        post_id = posts.insert_one(post).inserted_id
        print('Post ID: ', post_id)
