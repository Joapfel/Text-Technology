import re
import scrapy

class PublicationsSpiderAIMS(scrapy.Spider):
    name = 'publications_aims'
    start_urls = [
        'http://www.ims.uni-stuttgart.de/forschung/publikationen/aims.html'
    ]

    def parse(self, response):
        for entry in response.xpath('//div[@id="text"]//table//p/span[string-length(text())>0]'):
            year = entry.xpath('./strong/text()').extract_first()
            year = int(re.findall('\d{4}', year)[0])
            yield {
                'Year': year,
                'Title': entry.xpath('./text()').extract_first()
            }
