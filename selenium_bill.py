from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import re
import csv


csv_filename = "billboard_chart.csv"
csv_open = open(csv_filename, "w+", encoding="utf-8")
csv_writer = csv.writer(csv_open)
csv_writer.writerow(("rank", "title", "singer", "img"))


site_url = "https://www.billboard.com/charts/hot-100"
driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.implicitly_wait(20)
driver.get(site_url)




site_body = driver.find_element_by_css_selector("body")

for i in range(20):
    site_body.send_keys(Keys.PAGE_DOWN)
    sleep(3)


html = driver.page_source

driver.quit()

bs = BeautifulSoup(html, "html.parser")


total_list = bs.find_all("li", {"class" : re.compile("chart-list__element*")})


#print(total_list)


for i in total_list:
    rank = i.select_one("li > button > span.chart-element__rank.flex--column.flex--xy-center.flex--no-shrink > span.chart-element__rank__number").text
    song = i.select_one("li > button > span.chart-element__information > span.chart-element__information__song.text--truncate.color--primary").text
    artist = i.select_one("li > button > span.chart-element__information > span.chart-element__information__artist.text--truncate.color--secondary").text
    img = i.select_one("li > button > span.chart-element__image.flex--no-shrink")["style"].split('"')[1]
    #print(img)
    csv_writer.writerow((rank, song, artist, img))

csv_open.close()





