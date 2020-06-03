from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request
import requests
import re
import csv

csv_filename = "billboard_chart.csv"
csv_open = open(csv_filename, "w+", encoding="utf-8")
csv_writer = csv.writer(csv_open)
csv_writer.writerow(("rank", "title", "singer", "img"))

driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.implicitly_wait(3) #3초기다림
driver.get("https://www.billboard.com/charts/hot-100")


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
reque = urllib.request.Request("https://www.billboard.com/charts/hot-100", headers = headers)

html_doc = urllib.request.urlopen(reque)

bs = BeautifulSoup(html_doc, "html.parser",)


rank_select = bs.select("li > button > span.chart-element__rank.flex--column.flex--xy-center.flex--no-shrink > span.chart-element__rank__number")

title_select = bs.select("li > button > span.chart-element__information > span.chart-element__information__song.text--truncate.color--primary")
singer_select = bs.select("li > button > span.chart-element__information > span.chart-element__information__artist.text--truncate.color--secondary")
img = find_element_by_xpath("//*[@id=""charts""]/div/div[9]/ol/li[1]/button/span[3]")
print(img)
      


for i in zip(rank_select, title_select, singer_select):
    rank = i[0].text
    title = i[1].text
    singer = i[2].text
    csv_writer.writerow((rank, title, singer, img_select))




#title = bs.find_all(class_="chart-element__information__song text--truncate color--primary")

#for article in bs.find_all("span"):
    #rank = article.get("chart-element__rank__number")
    #title = article.get("chart-element__information__song text--truncate color--primary")


    #print(real_rank)
csv_open.close()

