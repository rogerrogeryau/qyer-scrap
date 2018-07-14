# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy_splash import SplashRequest
from scrapy.http import Request, FormRequest

class QyerSpiderSpider(scrapy.Spider):
	#Specify headers
	# headers = {
	# 	'X-Crawlera-Max-Retries': 1
	# }
	name = 'qyer-spider'
	allowed_domains = ['plan.qyer.com']
	start_urls = ["http://plan.qyer.com/search_0_0_11_0_0_0_0/?cityid=11186"]
	

	############################################################################################################
	# #previous version 
	# def parse(self, response):
	# 	if response.xpath('//*[@class="notext fontYaHei"]/text()').extract_first() is None:
	# 		items = response.xpath('//*[@class = "list"]/*[@class = "items"]')
			
	# 		for item in items:
	# 			num_of_day = item.xpath('.//*[@class = "day"]/strong/text()').extract_first()
	# 			places = item.xpath('.//*[@class = "plan"]/p/text()').extract_first()
	# 			num_of_view = item.xpath('.//*[@class = "icon1"]/text()').extract_first()
	# 			num_of_reply = item.xpath('.//*[@class = "icon2"]/text()').extract_first()
	# 			title_of_itin = item.xpath('.//dd/text()').extract_first()



	# 			yield{'num_of_day':num_of_day,
	# 				  'places':places,
	# 				  'num_of_view':num_of_view,
	# 				  'num_of_reply':num_of_reply,
	# 				  'title_of_itin':title_of_itin
	# 				  }

	# 	if response.xpath('//*[@class = "ui_page_item ui_page_next"]//text()').extract_first() == '下一页':
	# 		next_page_url = response.xpath('//*[@class = "ui_page_item ui_page_next"]//@href').extract_first()
	# 		yield Request(next_page_url, callback = self.parse)
	###########################################################################################################


	def parse(self, response):
		items_links = response.xpath('//*[@class="link"]/@href').extract()
		for item_link in items_links:
			absolute_item_link = response.urljoin(item_link)
			#click to the thread page for futher crawling
			yield Request(absolute_item_link, callback = self.parse_thread_content)

		#proceed to the next page
		next_page_url = response.xpath('//*[@class = "ui_page_item ui_page_next"]//@href').extract_first()
		yield Request(next_page_url)


	#thread content scrap
	def parse_thread_content(self, response):
		itin_items = response.xpath('//section/div[@class = "day"]')
		for itin_item in itin_items:
			day_of_itin = itin_item.xpath('./header/h2/text()').extract_first()
			print (day_of_itin)




		

		




	

