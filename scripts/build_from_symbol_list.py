import requests
import pandas as pd
from io import StringIO
import json


"""
FORMAT:
{
    TOKEN_MINT: {
        name: NAME,
        symbol: SYMBOL,
        decimals: DECIMALS,
        logo: LOGO_URI,
    }
}
"""

JUP_VALIDATED_TOKENS_URI = "https://raw.githubusercontent.com/jup-ag/token-list/main/validated-tokens.csv"
response = requests.get(JUP_VALIDATED_TOKENS_URI)
assert response.status_code == 200
token_list_csv = pd.read_csv(StringIO(response.text))

name_array = token_list_csv["Name"].tolist()
symbol_array = token_list_csv["Symbol"].tolist()
mint_array = token_list_csv["Mint"].tolist()
decimals_array = token_list_csv["Decimals"].tolist()
logo_array = token_list_csv["LogoURI"].tolist()


SOLANA_TOKENS_URI = "https://raw.githubusercontent.com/solana-labs/token-list/main/src/tokens/solana.tokenlist.json"
response_solana = requests.get(SOLANA_TOKENS_URI)
assert response_solana.status_code == 200
solana_token_list = response_solana.json()["tokens"]

for obj in solana_token_list:
    if obj["chainId"] == 101:
        solana_name = obj["name"]
        solana_symbol = obj["symbol"]
        solana_mint = obj["address"]
        solana_decimals = obj["decimals"]
        solana_logo = obj["logoURI"]
        if solana_mint not in mint_array:
            name_array.append(solana_name)
            symbol_array.append(solana_symbol)
            mint_array.append(solana_mint)
            decimals_array.append(solana_decimals)
            logo_array.append(solana_logo)

token_list_json = {
    symbol_array[i]: {
        "address": mint_array[i],
        "name": name_array[i],
        "decimals": decimals_array[i],
        "logoURI": logo_array[i]
    }
    for i in range(len(name_array))
}

with open("./from-symbol-token-list.json", "w") as file:

    json.dump(token_list_json, file, indent=4)
