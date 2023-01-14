import json
import os
from typing import Dict, Union
from dotenv import load_dotenv, find_dotenv

import requests


def get_oanda_price(instrument: str) -> float:
    """
    Get current price from Oanda API
    instrument: currency pair, eg. 'EUR_USD'
    """
    load_dotenv(find_dotenv())
    url: str = f'https://api-fxpractice.oanda.com/v3/instruments/{instrument}/candles'
    headers: Dict[str, str] = { "Authorization": f"Bearer {os.getenv('API_KEY')}"}
    r: requests.Response = requests.get(url, headers=headers)
    data: Dict[str, Union[str, float]] = json.loads(r.text)

    return float(data['candles'][0]['mid']['c'])