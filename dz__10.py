import sqlite3
import requests
from bs4 import BeautifulSoup

resp = requests.get("https://www.meteoprog.ua/ru/weather/Chernigiv/")

if resp.status_code == 200:
    soup = BeautifulSoup(resp.text, features="html.parser")
    soup_list = soup.find_all("div", {"class": "today-temperature"})
    res = soup_list[0].find("span")
    print("Зараз у Чернігові:", res.text, "C")
    soup_list = soup.find_all("section", {"class": "today-block white-icons block-weather-bg-day_snow"})
    res1 = soup_list[0].find("time")
    print("Зараз:", res1.text)

connection = sqlite3.connect("weather_cher.sl3", 5)
cur = connection.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS weather (дата_й_час TEXT, температура TEXT)")
connection.commit()

connection.close()
