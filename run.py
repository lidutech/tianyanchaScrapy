#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'stringk'
__mtime__ = '2018/9/26'
# qq:2456056533

佛祖保佑  永无bug!

"""


def run_spider():
    from scrapy import cmdline
    from tianyanchaScrapy.spiders.tianyancha import tyurl_spider
    from tianyanchaScrapy.spiders.tianyanchaDetail import tydetail_spider
    cmdline.execute('scrapy crawl {}'.format(tydetail_spider).split())


def run_all2():
    from scrapy.crawler import CrawlerRunner
    from scrapy.utils.project import get_project_settings
    from twisted.internet import reactor, defer
    from tianyanchaScrapy.spiders.tianyancha import TianyanchaSpider
    from tianyanchaScrapy.spiders.tianyanchaDetail import TianyanchaDetailSpider

    settings = get_project_settings()
    runner = CrawlerRunner(settings)

    @defer.inlineCallbacks
    def crawl():
        yield runner.crawl(TianyanchaSpider)
        yield runner.crawl(TianyanchaDetailSpider)
        reactor.stop()

    crawl()
    reactor.run()


if __name__ == '__main__':
    # run_spider()
    run_all2()
