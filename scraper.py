from wsgiref import headers
from selenium import webdriver
from bs4 import BeautifulSoup
import time 
import csv

START_URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)
time.sleep(10)

def scrape():
    headers=["Name","Distance","Mass","Radius"]
    soup=BeautifulSoup(browser.page_source,html.parser)
    for li_tag in soup.find_all("li",attrs={"class","Sun"}):
        td_tags=li_tag.find_all("td")
        templist=[]
        for index,td_tag in enumerate(td_tags):
            if index==0:
                templist.append(td_tag.find_all("a")[0].contents[0])
            else:
                try:
                    templist.append(td_tag.contents[0])
                except:
                    temp_list.append("")
        stars_data.append(templist)
    browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nev/span[2]/a').click()                    
   with open ("scraper2.csv","w")as f:
    csvwrite=csv.writer(f)
    csvwriter.writerows(headers)
    csvwriter.writerows(stars_data)
scrape()    



    