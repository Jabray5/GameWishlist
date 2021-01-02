import requests
from bs4 import BeautifulSoup
import json


def get_app_id_by_query(query):
    res = requests.get("https://store.steampowered.com/search/?term=" + query)
    soup = BeautifulSoup(res.content, "html.parser")
    return soup.find('a', class_="search_result_row ds_collapse_flag")['data-ds-appid']


def get_app_name(game_id):
    res = requests.get("https://store.steampowered.com/app/" + game_id)
    soup = BeautifulSoup(res.content, "html.parser")
    return soup.find('div', class_="apphub_AppName").text

def get_app_price(game_id, country_code):
    url = "https://store.steampowered.com/api/appdetails?appids=" + game_id + "&cc=" + country_code
    res = requests.get(url)
    price = json.loads(res.content)[game_id]["data"]["price_overview"]
    return price



