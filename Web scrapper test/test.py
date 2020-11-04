import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %matplotlib inline

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# url = "https://www.sofascore.com/pt/futebol/2018-09-18"

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
# {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

# This one does not get the actual transactions for the site
reg_url = "https://etherscan.io/token/0xaf9f549774ecedbd0966c52f250acc548d3f36e5?a=0xe8f063c4dc60b2f6c2c900d870ddcdae7daab7f6"

# req = Request(url=reg_url, headers=headers) 
# html = urlopen(req).read() 
# soup = BeautifulSoup(html, "lxml")

# This one doesn't work -- doesn't get the info we need -- just need to try more!! (SHOULD BE THE WAY)
table_class_name = 'table table-md-text-normal table-hover mb-4'
options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu') # add at the end?
# driver = webdriver.Chrome(options=options)
# driver.get(reg_url) ## has to be url directly?
# time.sleep(100) # Can adjust the length of sleep?
# page = driver.page_source
# driver.quit()
# soup = BeautifulSoup(page, 'lxml')

# Another way to use driver
driver = webdriver.Chrome()
driver.get(reg_url)
time.sleep(20)

# wait = WebDriverWait(driver, 100)
# element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, table_class_name)))
# element = wait.until(EC.presence_of_element_located((By.ID, 'maindiv')))
# HTML from element with some JavaScript
# element = driver.find_element_by_css_selector(table_class_name)
# html = driver.execute_script("return arguments[0].innerHTML;", element)

# print(html)

# html_code = driver.find_element('id','maindiv')
# print(html_code)

body = driver.find_element_by_tag_name('body')
print(body)

page = driver.page_source
driver.quit()
soup = BeautifulSoup(body, 'lxml')

# TESTS TO FIND THE ELs
# div1 = soup.find_all('div', attrs={'id': 'maindiv'})
# print("div: ", div1)

# div2 = soup.find_all('div', attrs={'class': 'table-responsive mb-2 mb-md-0'})
# print("div: ", div2)

# table = soup.find_all('table', attrs={'class': 'table table-md-text-normal table-hover mb-4'})
# print("table: ", table)



title = soup.title
print(title.text)

# links = soup.find_all('a', href=True)
# for link in links:
#     print(link.get("href"))

# print(soup)

# col_header = soup.find_all('th')
# print(col_header)

# test = soup.find_all('body')
# print(test)

data = []
allrows = soup.find_all("tr")
# print(allrows)
for row in allrows:
    row_list = row.find_all("td")
    dataRow = []
# print(row_list)
    for cell in row_list:
        #print(cell.text)
        dataRow.append(cell.text)
    data.append(dataRow)

overall_info = data[:4]
transactions = data[5:]

#print(data[5:50])
df = pd.DataFrame(transactions)
print(df.head(2))
print(df.tail(2))


print("\nthis acutally works")