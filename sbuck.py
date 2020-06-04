from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import re
import csv

csv_filename = "starbucks.csv"
csv_open = open(csv_filename, "w+", encoding="utf-8")
csv_writer = csv.writer(csv_open)
csv_writer.writerow(("drink_name", "img"))

site_url = "https://www.starbucks.co.kr/menu/drink_list.do"
driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.implicitly_wait(18)
driver.get(site_url)


site_body = driver.find_element_by_css_selector("body")

for i in range(18):
    site_body.send_keys(Keys.PAGE_DOWN)
    sleep(3)


html = driver.page_source

driver.quit()

bs = BeautifulSoup(html, "html.parser")

total_list = bs.find_all("li", {"class" : re.compile("menuDataSet")})
#print(total_list)

for i in total_list:
    drink_name = i.select_one("#container > div.content > div.product_result_wrap.product_result_wrap01 > div > dl > dd > div.product_list > dl > dd > ul > li > dl > dd").text
    img = i.select_one("#container > div.content > div.product_result_wrap.product_result_wrap01 > div > dl > dd > div.product_list > dl > dd > ul > li > dl > dt > a > img")["src"]
    csv_writer.writerow((drink_name, img))




csv_open.close()