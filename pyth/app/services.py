import requests
from .config import Config
from .utils import paginate

def get_coins(page_num=1, per_page=10):
    url = "https://api.coingecko.com/api/v3/coins/list"
    headers = {"accept": "application/json", "Authorization": f"Bearer {Config.COINGECKO_API_KEY}"}
    response = requests.get(url, headers=headers)
    data = response.json()
    return paginate(data, page_num, per_page)

def get_categories(page_num=1, per_page=10):
    url = "https://api.coingecko.com/api/v3/coins/categories/list"
    headers = {"accept": "application/json", "Authorization": f"Bearer {Config.COINGECKO_API_KEY}"}
    response = requests.get(url, headers=headers)
    data = response.json()
    return paginate(data, page_num, per_page)

def get_coin_details(coin_id):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
    headers = {"accept": "application/json", "Authorization": f"Bearer {Config.COINGECKO_API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()