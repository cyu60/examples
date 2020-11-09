import pandas as pd
import time
from datetime import datetime, timedelta
import useAPI

BASE_URL = "etherscan.io/"
CONTRACT = "0xaf9f549774ecedbd0966c52f250acc548d3f36e5"
req_address = "?a="
# aims to truncate dfs

def truncate_strings_for_display(df, columns):
    df1 = df.copy(deep=True)
    for i in columns:
        df1[i + '_display'] = df1[i].str.slice(0, 10)
        df1[i + '_display'] = df1[i + '_display'].astype(str) + '...'
    # print("from display\n", df1['from_display'],)
    return df1


def sort_value(df):
    return df.sort_values(by=['value'], ascending=False)

def clean_df(df):
    columns = ['hash', 'from', 'to']
    df = truncate_strings_for_display(df, columns)
    df = sort_value(df)
    return df

# DEPRICATED
# base url + api
def add_url_df(df):
    df1 = df.copy(deep=True)
    df1['hash_url'] = BASE_URL + 'tx/' + df1['hash'].astype(str) 
    df1['from_url'] = BASE_URL + 'token/' + CONTRACT + req_address + df1['from'].astype(str) 
    df1['to_url'] = BASE_URL + 'token/' + CONTRACT + req_address + df1['to'].astype(str) 
    # df1.drop(columns=['hash', 'from', 'to'], inplace=True)
    return df1

def adjust_sig_fig(df, col, num_fig):
    df[col] = df[col].astype(float) / (10 ** num_fig)

def display_df(df):
    df1 = add_url_df(df)
    return clean_df(df1)

if __name__ == "__main__":
    pass
