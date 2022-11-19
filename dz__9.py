import requests
from bs4 import BeautifulSoup

resp = requests.get("https://www.meteoprog.ua/ru/weather/Chernigiv/")

if resp.status_code == 200:
    soup = BeautifulSoup(resp.text, features="html.parser")
    soup_list = soup.find_all("div", {"class": "today-temperature"})
    res = soup_list[0].find("span")
    print("Зараз температура у Чернігові:", res.text, "С")
    soup_list = soup.find_all("section", {"class": "today-block white-icons block-weather-bg-day_snow"})
    res1 = soup_list[0].find("time")
    print("Зараз:", res1.text)