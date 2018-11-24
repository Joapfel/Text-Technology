import scrapy
import re

class PublicationsSpiderVerbmobil(scrapy.Spider):
    name = 'publications_verbmobil'
    start_urls = [
        'http://www.ims.uni-stuttgart.de/forschung/publikationen/verbmobil/index.html' 
    ]

    def parse(self, response):
        prevyear = ''
        for section in response.xpath('//div[@id="text"]/*[self::h3 or self::p]'):
            item = ''.join(section.xpath('.//text()').extract()).strip()
            year = re.findall('\d{4}', item)
            if year and len(item) < 6:
                prevyear = int(year[0])
            else:
                if prevyear and item:
                    yield{
                        'Year': prevyear,
                        'Title': item
                    }
