import requests
from bs4 import BeautifulSoup
import json


def get_app_id_by_query(query):
    # Currently gets the first name in the search result, this is a problem when games have sequels with similar names,
    # i.e. "Super Meat Boy" will grab "Super Meat Boy Forever" currently due to Steam's ranking
    res = requests.get("https://store.steampowered.com/search/?term=" + query)
    soup = BeautifulSoup(res.content, "html.parser")
    return soup.find('a', class_="search_result_row ds_collapse_flag")['data-ds-appid']


def get_app_name(game_id):
    res = requests.get("https://store.steampowered.com/app/" + game_id)
    soup = BeautifulSoup(res.content, "html.parser")
    return soup.find('div', class_="apphub_AppName").text


def get_current_price(game_id, country_code):
    url = "https://store.steampowered.com/api/appdetails?appids=" + game_id + "&cc=" + country_code
    res = requests.get(url)
    price = json.loads(res.content)[game_id]["data"]["price_overview"]['final'] / 100
    return price


def get_base_price(game_id, country_code):
    url = "https://store.steampowered.com/api/appdetails?appids=" + game_id + "&cc=" + country_code
    res = requests.get(url)
    price = json.loads(res.content)[game_id]["data"]["price_overview"]['initial'] / 100
    return price


def get_currency_by_country_code(country_code):
    url = "https://store.steampowered.com/api/appdetails?appids=219740" + "&cc=" + country_code
    res = requests.get(url)
    currency = json.loads(res.content)["219740"]["data"]["price_overview"]["currency"]
    return currency


def get_discount_amount(game_id, country_code):
    url = "https://store.steampowered.com/api/appdetails?appids=" + game_id + "&cc=" + country_code
    res = requests.get(url)
    discount_amount = json.loads(res.content)[game_id]["data"]["price_overview"]["discount_percent"]
    return discount_amount