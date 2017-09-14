from scrapy.spiders import CrawlSpider
from ..items import KuwoItem
from scrapy.selector import Selector
from scrapy.http import Request
import re
class Kuwo(CrawlSpider):
    name = "kuwo"
    start_urls = [
        "http://www.kuwo.cn/geci/l_23854431"
    ]
    url = start_urls[0]
    trigger = 1

    def parse(self, response):
        item = KuwoItem()
        selector = Selector(response)
        lyrics = selector.xpath('//*[@id="lrc_yes"]/text()').extract()
        info = lyrics[0]
        item['song'] = info.split(" - ")[0]
        item['singer'] =  info.split(" - ")[1]
        item['lyric'] = lyrics
        yield item
        
        if self.trigger == 1:
            self.trigger = 0
            for i in range(23854431,23854431+3000000):
                Link = "http://www.kuwo.cn/geci/l_"    
                request = Link + str(i)
                item['hao'] = request
                print request
                yield Request(request, callback= self.parse)
        # 24216116 - 23854431
        # param = self.counter
        # Link = "http://www.kuwo.cn/geci/l_"
        # item['bianhao'] = param
        # request = "http://www.kuwo.cn/geci/l_"+ str(param)
        # if param < 23854500:
        #     counter = self.counter + 1
        #     print request
        #     yield Request(request,callback=self.parse) 

        # l_24933975
        # 27392780
        # l_27389334
        # print param
            # 1141
