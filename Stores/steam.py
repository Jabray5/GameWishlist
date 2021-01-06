import requests
from bs4 import BeautifulSoup
import json


def get_app_id_by_query(query):
    # Gets multiple search results and tries to find best match
    res = requests.get("https://store.steampowered.com/search/?term=" + query)
    soup = BeautifulSoup(res.content, "html.parser")
    results = soup.find_all('a', class_="search_result_row ds_collapse_flag")

    for result in results:
        if result.find("span", class_="title").text.lower() == query.lower():
            return result['data-ds-appid']
    return results[0]['data-ds-appid']


def get_app_name(game_id):
    res = requests.get("https://store.steampowered.com/app/" + game_id)
    soup = BeautifulSoup(res.content, "html.parser")
    name = soup.find('div', class_="apphub_AppName").text
    # Should implement a list of problem characters here to be removed
    name = name.replace('®', '')
    return name


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
