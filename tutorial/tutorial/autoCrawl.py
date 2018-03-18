from scrapy.crawler import CrawlerProcess, Crawler, CrawlerRunner
from scrapy.settings import Settings
from scrapy.utils.project import get_project_settings
from scrapy import signals
from datetime import datetime
from threading import Timer
import pprint
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import http.client, urllib
import time
import datetime
import multiprocessing as mp
from multiprocessing import Process, Queue

from twisted.internet import reactor

import sys
#sys.path.insert(0, '/spiders/quotes_spider')
from spiders.quotes_spider import QuotesSpider
from scrapy.utils.log import configure_logging

TIME_START_END = {
    'mon': [datetime.time(7, 00), datetime.time(8, 0)],
    'tue': [datetime.time(7, 00), datetime.time(8, 0)],
    'wed': [datetime.time(7, 00), datetime.time(8, 0)],
    'thu': [datetime.time(7, 00), datetime.time(8, 0)],
    'fri': [datetime.time(7, 00), datetime.time(8, 0)],
    'sat': [datetime.time(8, 00), datetime.time(9, 0)],
    'sun': [datetime.time(8, 00), datetime.time(16, 0)],
}


def timer(firstTimeBool, day_polled):
    sleep_hour = 3600
    sleep_10_min = 600
    sleep_1_min = 60
    sleep_10_sec = 3

    print('hihi')
    while True:
        print('hihi')
        weekday = time.strftime('%a').lower()
        time_start, time_end = TIME_START_END[weekday]
        now = datetime.datetime.now().time()
        if time_start <= now <= time_end:
            print('We are in time')
            today = time.strftime('%m-%d')
            if day_polled == today:
                print('Already notified today!')
                sleep_time = sleep_hour
                time.sleep(sleep_hour)
            else:
                print('Lets notify')
                msg = setUpDatabaseConnectionRetrive(firstTimeBool)
                sendNotify(msg)
                #day_polled = today

                #Temp
                sleep_time = sleep_1_min
                time.sleep(sleep_time)
        else:
            print('It is not time!')
            sleep_time = sleep_10_min
            time.sleep(sleep_time)

def setUpDatabaseConnectionRetrive(firstTimeBool):
    if firstTimeBool == True:
        client = MongoClient()
        client = MongoClient('localhost', 27017)
        client = MongoClient('mongodb://localhost:27017/')
        db = client['mydb']
        collection = db.test_collection
        collection = db['test-collection']
        firstTimeBool = False
    else:
        db = client['mydb']
        collection = db.test_collection
        collection = db['test-collection']

    post = db.posts.find().sort('day',pymongo.DESCENDING)[0]
    msg = post.get("rain")
    return msg


def sendNotify(msg):
    print('Trying to push!')
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
      urllib.parse.urlencode({
        "token": "anho9ycivxnw86p774i9qsc2to78ym",
        "user": "u8xx2b59ao8nvuancemrx8p4tegx9g",
        "message": msg,
      }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()


if __name__ == '__main__':
    print('Running')
    day_polled = ''
    firstTimeBool = True
    timer(firstTimeBool, day_polled)
