import requests
import pandas as pd
import time
from datetime import datetime, timedelta

apikey = "C8WN32SD2E8C71KGTANNBZFDVJFM5KQGNM"
contract_address = "0xaf9f549774ecedbd0966c52f250acc548d3f36e5"

# Get user input
value_threshold = int(input("Enter the value threshold: "))
hours_ago_input = int(input("Enter the number of hours ago: "))
min_ago_input = int(input("Enter the number of min ago: "))


# event log?
# url = 'https://api.etherscan.io/api?module=logs&action=getLogs' + \
#     '&fromBlock=11194000' + \
#     '&toBlock=latest' + \
#     '&address=' + contract_address + \
#     '&apikey=' + apikey
# '&topic0=0xf63780e752c6a54a94fc52715dbc5518a3b4c3c2833d301a204226548a2a8545' + \

# Chainlink, Kylin

# Get the starting block
hours_ago = hours_ago_input
min_ago = hours_ago * 60 + min_ago_input
min_ago_time_stamp = 60 * min_ago
time_ago = str(int(time.time()) - min_ago_time_stamp)
# print(time_ago)

# Get Block Number by Timestamp
block_req = "https://api.etherscan.io/api?module=block&action=getblocknobytime" + \
    "&timestamp=" + time_ago + \
    "&closest=before" + \
    "&apikey=" + apikey

res_block = requests.get(block_req)
block_content = res_block.json()
start_block = block_content.get("result")

# token transfer events

trans_req = 'https://api.etherscan.io/api?module=account&action=tokentx' + \
    '&contractaddress=' + contract_address + \
    '&startblock=' + start_block + \
    '&endblock=latest'+ \
    '&sort=asc' + \
    '&apikey=' + apikey
# '&address=' + contract_address + \



response = requests.get(trans_req)
address_content = response.json()
result = address_content.get("result")

df = pd.DataFrame(result)

tokenDecimal = 18

df1 = df[['from', 'to', 'value']]
df1['value'] = df1['value'].astype(float) / (10 ** tokenDecimal)
# value_threshold = 2000


df2 = df1.loc[(df1['value'] >= value_threshold)]

print(df2)

df2.to_csv('filter_data.cvs')

# print(df1)
# print(df.head())

# tests = ['0xa8883787fae46e54d905a2e9eb31d8a02530f7af', 
#         '0xe8f063c4dc60b2f6c2c900d870ddcdae7daab7f6',
#         '0xe8509b1f74f2024ab52f423a6568ed5aace87c32',
#         '0x15848c6f03195e84e6a142ae4b4d56531150ff3d',
#          '0x1d53f08a4c05104763a65f2f8189d1cf29070008']


# for test in tests:
#     print(df1.loc[df['from'] == test])
#     print(df1.loc[df['to'] == test])
    # print(df1.loc[df['from'] == test].values)

# print(df.iloc[362])
# print(df.tail())

# print(df.columns)
# pd.set_option('display.max_colwidth', -1)
# print(df1['from'].tail(5))
# print(df.head(1).values)