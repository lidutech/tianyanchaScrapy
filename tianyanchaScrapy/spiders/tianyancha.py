# -*- coding: utf-8 -*-
import scrapy
from redis import Redis


from settings import REDIS_HOST

tyurl_spider = 'tyurl'

class TianyanchaSpider(scrapy.Spider):
    name = tyurl_spider
    allowed_domains = ['tianyancha.com']
    # start_urls = ['http://tianyancha.com/']

    redis_key = 'tyc:request'
    redis = Redis(host=REDIS_HOST)
    base_url = 'https://www.tianyancha.com/search/p{page}?key={key}'
    cookies = {}
    custom_settings = {'DOWNLOADER_MIDDLEWARES': {'tianyanchaScrapy.middlewares.UserAgentDownloaderMiddleware': 543, }}


    def fuzzy_search(self):
        '''
        模糊搜索
        :return: 
        '''
        # search_keys = ['软装', '家具', '民用家具', '酒店家具', '办公家具', '户外家具', '软装饰品', '软装灯饰', '软装墙饰', '软装吊饰', '软装画艺', '软装雕塑',
        #                '软装酒店用品', '软装花器', '软装窗帘', '软装床品', '软装抱枕靠垫', '软装墙布墙纸', '软装地毯', '软装餐布', '软装布艺', '软装花植花器', '软装鲜花绿植',
        #                '软装仿真干花']

        search_keys = ['软装']
        self.cookies = string_to_dict()
        for i in search_keys:
            for j in range(1, 6):  # 非会员(登不登录都只有5页,但是不登录容易被重定向到登录页)
                yield scrapy.Request(url=self.base_url.format(page=j, key=i), callback=self.url_parse,
                                     cookies=self.cookies)

    def key_search(self):
        '''
        关键字搜索
        :return: 
        '''
        from tianyanchaScrapy.other.fullname import get_name
        search_keys = get_name()
        self.cookies = string_to_dict()
        # for i in range(0,4):
        for i in range(0,len(search_keys)):
            yield scrapy.Request(url='https://www.tianyancha.com/search?key={}'.format(search_keys[i]), callback=self.url_parse,
                                     cookies=self.cookies)

    def start_requests(self):
        # self.fuzzy_search()
        # self.key_search()
        for request in self.fuzzy_search():
            yield request


    def url_parse(self, response):
        count = 0
        for i in response.xpath('//div[@class="search-result-single "]'):
            url = i.xpath('div[2]/div/a/@href').extract_first()
            if url:
                # count = self.redis.lpush(self.redis_key, url)
                count = self.redis.sadd(self.redis_key, url)


# 登录态
def string_to_dict():  # for cookies
    cookies = 'aliyungf_tc=AQAAAGc6IVIkcQkA47EPtzJx3cqvcD1d; csrfToken=5KSBHzOCbttFUO4IDw--d06s; TYCID=2a2ff340ca9a11e89380d7f4ada01077; undefined=2a2ff340ca9a11e89380d7f4ada01077; ssuid=3308074476; _ga=GA1.2.1380849203.1538962426; _gid=GA1.2.432350070.1538962426; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1538962423,1538965821; token=c49af420a3044304b20248cdc70fd850; _utm=a015f16aa06f45958a2d49577644e8fe; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNzc4ODU3MzAyMCIsImlhdCI6MTUzODk3Mjc2NiwiZXhwIjoxNTU0NTI0NzY2fQ.W91d3zPAXDCo8wvShPrJt_bwnu0JsOzaE-r71QrQCJCsr8YyD8W6amGIxn1tQHho3rugXcHsZo-kRhJ1gDFsQA%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252217788573020%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNzc4ODU3MzAyMCIsImlhdCI6MTUzODk3Mjc2NiwiZXhwIjoxNTU0NTI0NzY2fQ.W91d3zPAXDCo8wvShPrJt_bwnu0JsOzaE-r71QrQCJCsr8YyD8W6amGIxn1tQHho3rugXcHsZo-kRhJ1gDFsQA; _gat_gtag_UA_123487620_1=1; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1538972809'
    item_dict = {}
    items = cookies.split(';')
    for item in items:
        key = item.split('=')[0].replace(' ', '')
        value = item.split('=')[1]
        item_dict[key] = value

    return item_dict



if __name__ == '__main__':
    from scrapy.crawler import CrawlerProcess
    from scrapy.utils.project import get_project_settings

    # process = CrawlerProcess({'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'})
    process = CrawlerProcess(get_project_settings())
    process.crawl(TianyanchaSpider)
    process.start()