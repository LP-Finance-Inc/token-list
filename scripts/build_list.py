import requests
import pandas as pd
from io import StringIO
import json

def build_list():
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

    token_list_json = {
        mint_array[i]: {
            "name": name_array[i],
            "symbol": symbol_array[i],
            "decimals": decimals_array[i],
            "logo": logo_array[i]
        }
        for i in range(len(name_array))
    }

    with open("./token-list.json", "w") as file:

        json.dump(token_list_json, file, indent=4)
    return True