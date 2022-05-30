#!/usr/bin/env python3

##
## A tool that returns all the domains with
## a certain google analytics tag
##
## Written by Johannes Engren (@y0j33 on Twitter) 
## 


import requests
from bs4 import BeautifulSoup
import argparse

class TagDomains(object):
	def __init__(self,tag):
		self.tag = tag
		self.urls = []
	def run(self):
		r = requests.get("https://builtwith.com/relationships/tag/"+self.tag)
		soup = BeautifulSoup(r.text,'html.parser')
		table_soup = soup.find("table",class_="table").findAll("a")
		[self.urls.append(i.text) for i in table_soup]
	def __str__(self):
		return "".join([i+"\n" for i in self.urls])[:-1]

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Returns all the domains with a certain google analytics tag')
	parser.add_argument('--tag', '-t', help="google analytics tag")

	args=parser.parse_args()
	if(args.tag):
		d=TagDomains(args.tag)
		d.run()
		print(d)
	else:
		parser.print_help()

