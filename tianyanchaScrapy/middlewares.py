# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import base64

from scrapy import signals
import random

from .agents2 import AGENTS_ALL
class UserAgentDownloaderMiddleware:
    def process_request(self, request, spider):
        agent = random.choice(AGENTS_ALL)
        request.headers['User-Agent'] = agent
        # request.meta['proxy'] = 'http://ip:port'




class AbuyunProxyMiddleware(object):
    # 代理服务器
    proxyServer = "http://http-dyn.abuyun.com:9020"

    # 代理隧道验证信息
    proxyUser = "H4X82BC0EL1ZS69D"
    proxyPass = "85B833C15C8950BA"

    # for Python2
    # proxyAuth = "Basic " + base64.b64encode(proxyUser + ":" + proxyPass)

    # for Python3
    proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")

    def process_request(self, request, spider):
        request.meta["proxy"] = self.proxyServer
        request.headers["Proxy-Authorization"] = self.proxyAuth