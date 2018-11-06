# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random

from .agents2 import AGENTS_ALL
class UserAgentDownloaderMiddleware:
    def process_request(self, request, spider):
        agent = random.choice(AGENTS_ALL)
        request.headers['User-Agent'] = agent


