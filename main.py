#!/usr/bin/env python3

from bs4 import BeautifulSoup
from requests import request, post

class Item:
	
	def __init__(self, url):
		self.name, self.current_price, self.expiration_date, self.time_remaining = self.get_info(url)
		
	def get_info(self, url):
		html_doc = request("GET", URL).text
		soup = BeautifulSoup(html_doc, 'html.parser')
		
		item_name = soup.find("h2", class_="text-sm md:text-lg font-bold mb-4 cursor-pointer hover:text-bidfta-blue-light line-clamp-2").text
		current_price = soup.find("div", class_="text-xl font-semibold").text
		
		expiration_date_character_array = list(soup.find("div", class_="mb-1").text)
		expiration_date_character_array.insert(-12, "\n")
		expiration_date = "".join(expiration_date_character_array)
		
		time_remaining = soup.find("p", class_="font-bold uppercase leading-5 text-10 md:text-xs").text
		
		return item_name, current_price, expiration_date, time_remaining

def find_text_between(text, str1, str2):
	
	front_first = 0
	front_last = len(str1)
	back_first = len(text) - len(str2) - 1
	back_last = len(text)
	
	seek_front = text[front_first : front_last]
	seek_back = text[back_first : back_last]
	
	if seek_front == str1 and seek_back == str2:
		return text[len(str1):len(text) - len(str2)]
	else:
		find_text_between(text[1:-1], str1, str2)
		
		
URL = "https://www.bidfta.com/503611/item-detail/41677976"

item1 = Item(URL)

payload = {
	"name" : item1.name,
	"current_price" : item1.current_price,
	"expiration_date" : item1.expiration_date,
	"time_remaining" : item1.time_remaining
}

webhook_url = "https://maker.ifttt.com/trigger/bidfta_check/json/with/key/dS5MVmao4czu6gr1sk-jtQ"

resp = post(webhook_url, json=payload, timeout=5)
resp.raise_for_status()




print(item1.name)