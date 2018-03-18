from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from spiders.quotes_spider import QuotesSpider

def crawl_job():
    """
    Job to start spiders.
    Return Deferred, which will execute after crawl has completed.
    """
    print('crawl_job')
    settings = get_project_settings()
    runner = CrawlerRunner(settings)
    return runner.crawl(QuotesSpider)

def schedule_next_crawl(null, sleep_time):
    print('schedule_next_crawl')
    """
    Schedule the next crawl
    """
    reactor.callLater(sleep_time, crawl)

def crawl():
    print('crawl')
    """
    A "recursive" function that schedules a crawl 30 seconds after
    each successful crawl.
    """
    d = crawl_job()
    sleep_6_hour = 3600*6
    d.addCallback(schedule_next_crawl, sleep_6_hour)
    d.addErrback(catch_error)

def catch_error(failure):
    print(failure.value)


if __name__=="__main__":
    crawl()
    reactor.run()
