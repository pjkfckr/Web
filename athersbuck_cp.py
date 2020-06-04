from bs4 import BeautifulSoup
from selenium import webdriver
import re
import csv


csv_filename = "athersbucks.csv"
csv_open = open(csv_filename, "w+", encoding="utf-8")
csv_writer = csv.writer(csv_open)
csv_writer.writerow(("food_name", "image"))

url = "https://www.starbucks.co.kr/menu/food_list.do"
driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get(url)

html = driver.page_source

driver.quit()

bs = BeautifulSoup(html, "html.parser")


total_list = bs.select("#container > div.content > div.product_result_wrap.product_result_wrap01 > div > dl > dd > div.product_list > dl > dd > ul > li")


#print(total_list)

for i in total_list:
	food = i.find("dd").text
	img = i.find("img")["src"]
	csv_writer.writerow((food, img))




csv_open.close()
