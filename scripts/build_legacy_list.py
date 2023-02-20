import requests
import pandas as pd
from io import StringIO
import json

"""
FORMAT:
{
    "tokens": [
         {
            "chainId": 101,
            "address": "3SghkPdBSrpF9bzdAy5LwR4nGgFbqNcC6ZSq8vtZdj91",
            "symbol": "EV1",
            "name": "EveryOne Coin",
            "decimals": 9,
            "logoURI": "https://raw.githubusercontent.com/solana-labs/token-list/main/assets/mainnet/3SghkPdBSrpF9bzdAy5LwR4nGgFbqNcC6ZSq8vtZdj91/logo.png",
        },
    ]
}
"""
JUP_VALIDATED_TOKENS_URI = "https://raw.githubusercontent.com/jup-ag/token-list/main/validated-tokens.csv"

response = requests.get(JUP_VALIDATED_TOKENS_URI).text

token_list_csv = pd.read_csv(StringIO(response))

name_array = token_list_csv["Name"].tolist()
symbol_array = token_list_csv["Symbol"].tolist()
mint_array = token_list_csv["Mint"].tolist()
decimals_array = token_list_csv["Decimals"].tolist()
logo_array = token_list_csv["LogoURI"].tolist()

token_list_json = {
    "tokens": [
        {
            "chainId": 101, # mainnet
            "address": mint_array[i],
            "symbol": symbol_array[i],
            "name": name_array[i],
            "decimals": decimals_array[i],
            "logoURI": logo_array[i]
        }
    ]
    for i in range(len(name_array))
}

with open("../legacy-token-list.json", "w") as file:

    json.dump(token_list_json, file, indent=4)