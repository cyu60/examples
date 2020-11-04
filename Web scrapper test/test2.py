import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import pandas as pd

headers = {
    'authority': 'etherscan.io',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.58',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'iframe',
    'referer': 'https://etherscan.io/token/generic-tokentxns2?m=normal^&contractAddress=0xaf9f549774ecedbd0966c52f250acc548d3f36e5^&a=0xe8f063c4dc60b2f6c2c900d870ddcdae7daab7f6^&sid=e86225c83258667e39326cb474eff4fc^&p=1',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '__cfduid=da1db6de45915efe4385249b56d7e35a61601951742; _ga=GA1.2.483039272.1601951752; ASP.NET_SessionId=qyprrgnalevs14cnyjnhfafa; __cflb=0H28vPcoRrcznZcNZSuFrvaNdHwh858TRxiHds2zB7A; _gid=GA1.2.1760364558.1604463869',
}

params = (
    ('contractAddress', '0xaf9f549774ecedbd0966c52f250acc548d3f36e5^'),
    ('mode', '^'),
    ('sid', 'e86225c83258667e39326cb474eff4fc^'),
    ('a', '0xe8f063c4dc60b2f6c2c900d870ddcdae7daab7f6^'),
    ('m', 'normal^'),
    ('p', '2'),
)

req = Request('https://etherscan.io/token/generic-tokentxns2', headers=headers)

response = urlopen(req, timeout=20).read()
response_close = urlopen(req, timeout=20).close()
page_soup = soup(response, "html.parser")
Transfers_info_table_1 = page_soup.find("table", {"class": "table table-md-text-normal table-hover mb-4"})
df=pd.read_html(str(Transfers_info_table_1))[0]
df.to_csv("TransferTable.csv",index=False)
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://etherscan.io/token/generic-tokentxns2?contractAddress=0xaf9f549774ecedbd0966c52f250acc548d3f36e5^&mode=^&sid=e86225c83258667e39326cb474eff4fc^&a=0xe8f063c4dc60b2f6c2c900d870ddcdae7daab7f6^&m=normal^&p=2', headers=headers)