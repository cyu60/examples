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
req = Request(url=reg_url, headers=headers) 
# html = urlopen(req).read() 
# soup = BeautifulSoup(html, "lxml")

# This one doesn't work -- doesn't ge the info we need
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=options)
driver.get(reg_url) ## has to be url directly?
time.sleep(3)
page = driver.page_source
driver.quit()
soup = BeautifulSoup(page, 'html.parser')


title = soup.title
print(title.text)

# links = soup.find_all('a', href=True)
# for link in links:
#     print(link.get("href"))

print(soup)

# col_header = soup.find_all('th')
# print(col_header)

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