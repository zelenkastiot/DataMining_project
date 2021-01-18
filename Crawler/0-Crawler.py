"""

 Created on 10-Nov-20
 @author: David Ordevski

"""

class RealEstateSpider(scrapy.Spider):
    name = 'real_estate'
    user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
    start_urls = [
        'https://www.domain.com.au/sale/blue-mountains-and-surrounds-nsw/?price=0-850000&page=1',
    ]
 
    def parse(self, response):
        with open('real-estate.csv', 'a', newline='', encoding='UTF-8') as file:
            writer = csv.writer(file)
 
            #div.css-1n74r2t
            for estate in response.css('div.css-1gkcyyc'):
                price = estate.xpath('div/div/p/text()').get()
                street_address = estate.xpath('div//h2/span[1]/text()').get()
                address_locality = estate.xpath('div//h2/span[2]/span[1]/text()').get()
                address_region = estate.xpath('div/a/h2/span[2]/span[2]/text()').get()
                postal_code = estate.xpath('div/a/h2/span[2]/span[3]/text()').get()
                bedrooms = estate.xpath('div//div/span[1]/span/text()').get()
                bathrooms = estate.xpath('div//div/span[2]/span/text()').get()
                car_slots = estate.xpath('div//div/span[3]/span/text()').get()
                meters_squared = estate.xpath('div//div/span[4]/span/text()').get()
                type = estate.xpath('div/div/div[2]/span/text()').get()
 
 
                writer.writerow([price, street_address, address_locality, address_region,
                                 postal_code, bedrooms, bathrooms, car_slots, meters_squared, type])
 
 
 
        #div.css-1t2vh5b a::attr("href") , div.css-1uoq19z/a[2]::attr("href")
        next_page = response.css('').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)