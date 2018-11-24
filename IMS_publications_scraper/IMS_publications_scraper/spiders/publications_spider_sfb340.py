import re
import scrapy

class PublicationsSpiderSFB2(scrapy.Spider):
    name = "publications_sfb2"
    start_urls = [
        'http://www.sfs.uni-tuebingen.de/sfb/reports/sfb-pap.html' 
    ]

    def parse(self, response):
        for entry in response.xpath('//ol/li'):
            a = entry.xpath('./a')
            title = ''.join(entry.xpath('./text()').extract_first()).strip()
            if a:
                a = a.xpath('./text()').extract_first()
                li = entry.xpath('./text()').extract()
                title = ''.join([li[0].strip(), a.strip(), li[1].strip()])
            if title:
                year = re.findall('\d{4}', title)
                if year:
                    year = int(year[0])
                    title = title.split('('+str(year)+')')[0].strip()
                yield{
                    'Year': year,
                    'Title': title
                }
