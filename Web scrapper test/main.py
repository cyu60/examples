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


reg_url = "https://etherscan.io/token/0xaf9f549774ecedbd0966c52f250acc548d3f36e5?a=0xe8f063c4dc60b2f6c2c900d870ddcdae7daab7f6"

options = Options()
options.add_argument("start-maximized")
options.add_argument('--no-sandbox')
options.add_argument("--hide-scrollbars")
options.add_argument("disable-infobars")
options.add_argument('--disable-dev-shm-usage')
# options.add_argument("window-size=1920,1080")
# options.headless = True
# options.add_argument('--headless') # can't be headless or would lead to error

driver = webdriver.Chrome(options=options)
# driver.set_window_size(1200, 600)
driver.get(reg_url)

wait = WebDriverWait(driver, 10)
# frame = wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "tokentxnsiframe")))
frame = wait.until(EC.frame_to_be_available_and_switch_to_it(
    (By.XPATH, '//*[@id="tokentxnsiframe"]')))
    
frameSource = driver.page_source
driver.quit()

soup = BeautifulSoup(frameSource, 'lxml')

def extract(soup):
    data = []
    allrows = soup.find_all("tr")
    for row in allrows:
        row_list = row.find_all("td")
        dataRow = []
        for cell in row_list:
            dataRow.append(cell.text)
        data.append(dataRow)

    transactions = data[5:]

    df = pd.DataFrame(transactions)
    df.drop(columns=df.columns[[0, 1, 8]], inplace=True)
    print(df)

    # Sort out the headers -- tried finding it, but realized it was easier to hard code
    # header_list = []
    # col_headers = soup.find_all('th')

    # for col in col_headers:
    #     text = col.text.replace('\n', '')
    #     header_list.append(text)
    # print(header_list)
    header_list = ['Txn Hash', 'Age', 'From', 'DIR', 'To', 'Quantity']
    df.columns = header_list

    return df

# actual code

df = extract(soup)

for i in range(5): # range can be adjusted to get more info
    time.sleep(300) # delay can be adjusted
    ndf = extract(soup)
    pd.concat([df, ndf]).drop_duplicates().reset_index(drop=True)
    # need to drop duplicates

df2 = df.drop(columns=['Txn Hash', 'Age'])  # df.columns is zero-based pd.Index 
# print(df2)

df.to_csv('all_data.csv')
# df.to_csv('all_data.csv', encoding='utf-8')
df2.to_csv('concise_data.csv')
# df2.to_csv('concise_data.csv', encoding='utf-8')

# append in the future
# df.to_csv('my_csv.csv', mode='a', header=False)


print("\nthis acutally works")
