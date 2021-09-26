from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()
d = {}


def top_n_cryptocurrencies(n):
    coins = cg.get_coins_markets('usd')
    for i in range(n):
        c = coins[i]['id']
        t = cg.get_price(c, 'usd', include_market_cap=True)
        for k, v in t.items():
            for value in v.items():
                d[k] = value[1]
    d1 = sorted(d.items(), key=lambda x: x[1], reverse=True)
    for k, v in d1:
        print(k, v)


n = int(input("Enter a number "))
print(cg.get_price(ids='bitcoin', vs_currencies='usd'), '\n')
top_n_cryptocurrencies(n)

