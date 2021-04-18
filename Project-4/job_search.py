import scrapy

class SeekSpider(scrapy.Spider):
    name = "job_search"
    allowed_domains = ["seek.com.au"]
    start_urls = ['https://www.seek.com.au/data-science-jobs/in-All-Australia']
    
    def parse(self, response):
        print('-----------------')
        print('I just visited :' + response.url)
        print('-----------------')
        urls = response.css('h1 > a::attr(href)'.extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url = url, callback =self.parse_details)
        next_page = response.css('a[data-automation="page-next"]::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback = self.parse)

    def parse_details(self, response):
        yield {
            'title': response.css('span[data-automation="job-detail-title"] h1::text')[0].extract(),
            'date': response.css('dd[data-automation="job-detail-date"] span::text’)[1].extract(),
            'company': response.css('span[data-automation="advertiser-name"] span::text')[0].extract(),
            'location': response.css('strong._7ZnNccT::text')[1].extract(),
            'area': response.css('span._2TSaU36::text')[0].extract(),
            'salary': response.css('span._7ZnNccT::text')[1].extract(),
            'description': response.css('div[data-automation="mobileTemplate"] p::text').extract()
        }