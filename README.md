#Usage of library pycoingecko
___
We will filter out top N cryptocurrencies by market capitalization using library pycoingecko
####Installation
PyPI
```
pip install pycoingecko
```
or from source
```
git clone https://github.com/man-c/pycoingecko.git
cd pycoingecko
python3 setup.py install
```
####Usage
```
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
```
####Examples
```
# /simple/price endpoint with the required parameters
>>> cg.get_price(ids='bitcoin', vs_currencies='usd')
{'bitcoin': {'usd': 3462.04}}
```