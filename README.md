# LP Finance Token List
LP Finance created two tokens list formats, which can be adopted by simply replacing the [`solana-labs/token-list`](https://github.com/solana-labs/token-list) endpoint. Generated token lists are a wrapper of [`jup-ag/token-list`](https://github.com/jup-ag/token-list/tree/main) main branch.

Token lists do not include banned tokens flagged on Jupiter and solely use validated tokens as source.

## Legacy Token List
[`legacy-token-list.json`](https://raw.githubusercontent.com/LP-Finance-Inc/token-list/main/legacy-token-list.json) uses the data from Jupiter Aggregator token list and reformats to `solana-labs/token-list` structure.

Format
```
{
    "tokens": [
        {
            "chainId": 101, 
            "address": TOKEN_MINT,
            "symbol": SYMBOL,
            "name": NAME,
            "decimals": DECIMALS,
            "logoURI": LOGO_URI,
        },
    ]
}
```
## Token List
Format
```
{
    TOKEN_MINT: {
        "name": NAME,
        "symbol": SYMBOL,
        "decimals": DECIMALS,
        "logo": LOGO_URI,
    }
}
```
## Endpoints
### Legacy Token List
[https://raw.githubusercontent.com/LP-Finance-Inc/token-list/main/legacy-token-list.json](https://raw.githubusercontent.com/LP-Finance-Inc/token-list/main/legacy-token-list.json)
### Token List
[https://raw.githubusercontent.com/LP-Finance-Inc/token-list/main/token-list.json](https://raw.githubusercontent.com/LP-Finance-Inc/token-list/main/token-list.json)