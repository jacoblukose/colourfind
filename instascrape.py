
import re
import json
import requests
import sys 
import os
from time import sleep
import sys

from tzlocal import get_localzone
import iso8601
from datetime import datetime
from pytz import timezone

class instascrape:

	def __init__(self,username,number_of_post=20):
		
		self.username=username
		self.max_id=None
		self.post_num=0
		self.number_of_post=number_of_post

	def crawl(self):
		"""Crawls and downloads the images """

		if self.max_id is None:
			url = 'http://instagram.com/{}/media'.format(self.username)
		else:
			url='http://instagram.com/{}/media/?&max_id={}'.format(self.username,self.max_id)
		
		try:	
			resp=requests.get(url)
		except requests.exceptions.ConnectionError:
			sleep(5)
			resp=requests.get(url)
			
		data=json.loads(resp.text)
		self.download(data)
		
		if 'more_available' in data and data['more_available'] is True and self.post_num < self.number_of_post:
			self.max_id=data['items'][-1]['id']
			self.crawl()


	def download(self,data):

		"""Sets directory and filenames and downloads files """

		try:
			os.makedirs(self.username)
		except:
			pass
		
		if data['items']==[]:
			print "Private account ,cant download"
			return 
			
		for values in data['items']:
			url_temp=values["images"]['standard_resolution']['url']
			with open('{}/{}.jpg'.format(self.username,self.post_num), 'wb') as f:
				
				try:
					bytes = requests.get(url_temp).content
				except requests.exceptions.ConnectionError:
					sleep(5)
					bytes = requests.get(url_temp).content
				
				f.write(bytes)
				self.post_num=self.post_num+1
				sys.stdout.write('\rDownloaded {} images+{}'.format(self.post_num,values['caption']['created_time']))
				sys.stdout.flush()
			if self.number_of_post <= self.post_num:
				break
	


		

		

		

if __name__ == '__main__':

	

	# local_tz = get_localzone()
	# m=iso8601.parse_date(time)
	# time_utc=m.astimezone(timezone('UTC'))
	# local_time=time_utc.astimezone(local_tz)

	username =sys.argv[1]
	scraper=instascrape(username)
	scraper.crawl()