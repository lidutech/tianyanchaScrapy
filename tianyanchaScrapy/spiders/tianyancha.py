# -*- coding: utf-8 -*-
import scrapy
from redis import Redis


from tianyanchaScrapy.settings import REDIS_HOST

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
                                     cookies=self.cookies,dont_filter=True)

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
                                     cookies=self.cookies,dont_filter=True)

    def start_requests(self):
        # self.fuzzy_search()
        # self.key_search()
        for request in self.fuzzy_search():
            yield request


    def url_parse(self, response):
        count = 0
        for i in response.xpath('//div[@class="search-item sv-search-company"]/div'):
            url = i.xpath('div[3]/div/a/@href').extract_first()
            if url:
                # count = self.redis.lpush(self.redis_key, url)
                count = self.redis.sadd(self.redis_key, url)
                self.logger.info('sadd status:%s'%count)


# 登录态
def string_to_dict():  # for cookies
    cookies = 'aliyungf_tc=AQAAAGVrdjwgyAQAxkGNPcl9C14cudn5; TYCID=2b4ec0a0335c11e9a30557419ac693dc; undefined=2b4ec0a0335c11e9a30557419ac693dc; ssuid=1338268536; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1550480658; _ga=GA1.2.107372594.1550480658; _gid=GA1.2.760388699.1550480658; __insp_wid=677961980; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cudGlhbnlhbmNoYS5jb20v; __insp_targlpt=5aSp55y85p_lLeWVhuS4muWuieWFqOW3peWFt1%2FkvIHkuJrkv6Hmga%2Fmn6Xor6Jf5YWs5Y_45p_l6K_iX_W3peWVhuafpeivol%2FkvIHkuJrkv6HnlKjkv6Hmga%2Fns7vnu58%3D; __insp_ss=1550480658977; __insp_norec_sess=true; csrfToken=u7V3EhlQ5rdXTQlybm7Su-vo; bannerFlag=true; token=6347b527c74e42268d1d2ae69bbab8eb; _utm=b3d56926d93d4380802ebe538ad23922; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E8%2589%25BE%25E4%25BC%25A6%25C2%25B7%25E4%25BC%25AF%25E6%2596%25AF%25E6%25B1%2580%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A%25220%2522%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25220%2522%252C%2522monitorUnreadCount%2522%253A%2522105%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNzc4ODU3MzAyMCIsImlhdCI6MTU1MDQ4MTA2NiwiZXhwIjoxNTY2MDMzMDY2fQ.-fbJIa9EfV8BjM7kfXDEAGmcBtrGDZ7RzIO9EOpVfFMLuCS8W5UwZrnzUD3MyWv_lIKu_tTJuN3_lCNgW-mIFw%2522%252C%2522pleaseAnswerCount%2522%253A%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252217788573020%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNzc4ODU3MzAyMCIsImlhdCI6MTU1MDQ4MTA2NiwiZXhwIjoxNTY2MDMzMDY2fQ.-fbJIa9EfV8BjM7kfXDEAGmcBtrGDZ7RzIO9EOpVfFMLuCS8W5UwZrnzUD3MyWv_lIKu_tTJuN3_lCNgW-mIFw; RTYCID=e36e6c75e11a4d7a990c536242d631bd; CT_TYCID=0a4b25c4cc904f0196f69b6795bc25f2; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1550481471; __insp_slim=1550481470935; cloud_token=14e4908a2b8a45b59412860fe596ccab'
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