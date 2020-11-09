# MOVE TO DIFF MODULE
BASE_URL = "https://etherscan.io/"
CONTRACT = "0xaf9f549774ecedbd0966c52f250acc548d3f36e5"
req_address = "?a="


def build_url(data, col):
    if col == 'hash':
        return BASE_URL + 'tx/' + data
    else:
        return BASE_URL + 'token/' + CONTRACT + req_address + data
