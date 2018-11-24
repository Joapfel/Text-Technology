import scrapy
import re

class PublicationsSpiderSFB(scrapy.Spider):
    name = 'publications_sfb'
    start_urls = [
        'http://www.uni-stuttgart.de/linguistik/sfb732/index.php?article_id=5'
    ]

    def parse(self, response):
        for href in response.xpath('//div[@class="section"]/ul/li/a/@href'):
            yield response.follow(href, self.parse_volume)

    def parse_volume(self, response):
        r = response.xpath('//div[@class="section"]')
        year = ''.join(response.xpath('//div[@class="middle_headline"]/text()').extract())
        year = int(re.findall('\d{4}', year)[0])

        if int(float(r.xpath('count(./ul/li)').extract_first())) > 1:
            li_s = r.xpath('./ul/li')
            for li in li_s[1:]:
                title = li.xpath('./a/text()').extract_first()
                yield {
                    'Year': year,
                    'Title': title
                }
        else:
            title = ''.join(r.xpath('.//*[self::div or self::p or self::em or self::a]/text()').extract())
            title = title.replace('Entire volume', '')
            title_ = title.split('('+str(year)+'),')
            if len(title_) > 1:
                title = title_[1]
            yield {
                'Year': year,
                'Title': title.strip()
            }
