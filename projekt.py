from tkinter import *
from tkinter.ttk import Combobox
import requests
from bs4 import BeautifulSoup
from datetime import datetime

current_time = datetime.now()

resp = requests.get("https://meteo.ua/ua#2022-11-19--14-00")
resp1 = requests.get("https://meteo.ua/ua/6/chernigov#2022-11-19--14-00")
resp2 = requests.get("https://meteo.ua/ua/23/sumyi#2022-11-19--14-00")
resp3 = requests.get("https://meteo.ua/ua/31/jitomir#2022-11-19--14-00")
resp4 = requests.get("https://meteo.ua/ua/13/lutsk#2022-11-19--14-00")
resp5 = requests.get("https://meteo.ua/ua/28/rovno#2022-11-19--14-00")
resp6 = requests.get("https://meteo.ua/ua/44/lvov#2022-11-19--14-00")
resp7 = requests.get("https://meteo.ua/ua/67/ivano-frankovsk#2022-11-19--14-00")
resp8 = requests.get("https://meteo.ua/ua/83/uzhgorod#2022-11-19--14-00")
resp10 = requests.get("https://meteo.ua/ua/71/vinnitsa#2022-11-19--14-00")


def weather():
    town = box.get()
    if town == "Київ":
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, features="html.parser")
            soup_list = soup.find_all("div", {"class": "weather-detail__main-panel-left"})
            res = soup_list[0].find("div")
            label3 = Label(text=f"Темперетура: {str(res.text)} °C", font="Arial 19")
            label3.grid(row=3, column=0, padx=10, pady=10, sticky=NW)
            soup_list = soup.find_all("div", {"class": "weather-detail__extra-item"})
            op = soup_list[0].find("div", {"data-key": "fallout"})
            label4 = Label(text=f"Імовірність опадів: {str(op.text)}", font="Arial 19")
            label4.grid(row=4, column=0, padx=10, pady=10, sticky=NW)
    if town == "Чернігів":
        if resp1.status_code == 200:
            soup = BeautifulSoup(resp1.text, features="html.parser")
            soup_list = soup.find_all("div", {"class": "weather-detail__main-panel-left"})
            res1 = soup_list[0].find("div")
            label3 = Label(text=f"Темперетура: {str(res1.text)} °C", font="Arial 18")
            label3.grid(row=3, column=0, padx=10, pady=10, sticky=NW)
            soup_list = soup.find_all("div", {"class": "weather-detail__extra-item"})
            op = soup_list[0].find("div", {"data-key": "fallout"})
            label4 = Label(text=f"Імовірність опадів: {str(op.text)}", font="Arial 19")
            label4.grid(row=4, column=0, padx=10, pady=10, sticky=NW)
    if town == "Суми":
        if resp2.status_code == 200:
            soup = BeautifulSoup(resp2.text, features="html.parser")
            soup_list = soup.find_all("div", {"class": "weather-detail__main-panel-left"})
            res2 = soup_list[0].find("div")
            label3 = Label(text=f"Темперетура: {str(res2.text)} °C", font="Arial 18")
            label3.grid(row=3, column=0, padx=10, pady=10, sticky=NW)
            soup_list = soup.find_all("div", {"class": "weather-detail__extra-item"})
            op = soup_list[0].find("div", {"data-key": "fallout"})
            label4 = Label(text=f"Імовірність опадів: {str(op.text)}", font="Arial 19")
            label4.grid(row=4, column=0, padx=10, pady=10, sticky=NW)
    if town == "Житомир":
        if resp3.status_code == 200:
            soup = BeautifulSoup(resp3.text, features="html.parser")
            soup_list = soup.find_all("div", {"class": "weather-detail__main-panel-left"})
            res3 = soup_list[0].find("div")
            label3 = Label(text=f"Темперетура: {str(res3.text)} °C", font="Arial 18")
            label3.grid(row=3, column=0, padx=10, pady=10, sticky=NW)
            soup_list = soup.find_all("div", {"class": "weather-detail__extra-item"})
            op = soup_list[0].find("div", {"data-key": "fallout"})
            label4 = Label(text=f"Імовірність опадів: {str(op.text)}", font="Arial 19")
            label4.grid(row=4, column=0, padx=10, pady=10, sticky=NW)
    if town == "Луцьк":
        if resp4.status_code == 200:
            soup = BeautifulSoup(resp4.text, features="html.parser")
            soup_list = soup.find_all("div", {"class": "weather-detail__main-panel-left"})
            res4 = soup_list[0].find("div")
            label3 = Label(text=f"Темперетура: {str(res4.text)} °C", font="Arial 18")
            label3.grid(row=3, column=0, padx=10, pady=10, sticky=NW)
            soup_list = soup.find_all("div", {"class": "weather-detail__extra-item"})
            op = soup_list[0].find("div", {"data-key": "fallout"})
            label4 = Label(text=f"Імовірність опадів: {str(op.text)}", font="Arial 19")
            label4.grid(row=4, column=0, padx=10, pady=10, sticky=NW)
    if town == "Рівне":
        if resp5.status_code == 200:
            soup = BeautifulSoup(resp5.text, features="html.parser")
            soup_list = soup.find_all("div", {"class": "weather-detail__main-panel-left"})
            res5 = soup_list[0].find("div")
            label3 = Label(text=f"Темперетура: {str(res5.text)} °C", font="Arial 18")
            label3.grid(row=3, column=0, padx=10, pady=10, sticky=NW)
            soup_list = soup.find_all("div", {"class": "weather-detail__extra-item"})
            op = soup_list[0].find("div", {"data-key": "fallout"})
            label4 = Label(text=f"Імовірність опадів: {str(op.text)}", font="Arial 19")
            label4.grid(row=4, column=0, padx=10, pady=10, sticky=NW)
    if town == "Львів":
        if resp6.status_code == 200:
            soup = BeautifulSoup(resp6.text, features="html.parser")
            soup_list = soup.find_all("div", {"class": "weather-detail__main-panel-left"})
            res6 = soup_list[0].find("div")
            label3 = Label(text=f"Темперетура: {str(res6.text)} °C", font="Arial 18")
            label3.grid(row=3, column=0, padx=10, pady=10, sticky=NW)
            soup_list = soup.find_all("div", {"class": "weather-detail__extra-item"})
            op = soup_list[0].find("div", {"data-key": "fallout"})
            label4 = Label(text=f"Імовірність опадів: {str(op.text)}", font="Arial 19")
            label4.grid(row=4, column=0, padx=10, pady=10, sticky=NW)
    if town == "Івано-Франківськ":
        if resp7.status_code == 200:
            soup = BeautifulSoup(resp7.text, features="html.parser")
            soup_list = soup.find_all("div", {"class": "weather-detail__main-panel-left"})
            res7 = soup_list[0].find("div")
            label3 = Label(text=f"Темперетура: {str(res7.text)} °C", font="Arial 18")
            label3.grid(row=3, column=0, padx=10, pady=10, sticky=NW)
            soup_list = soup.find_all("div", {"class": "weather-detail__extra-item"})
            op = soup_list[0].find("div", {"data-key": "fallout"})
            label4 = Label(text=f"Імовірність опадів: {str(op.text)}", font="Arial 19")
            label4.grid(row=4, column=0, padx=10, pady=10, sticky=NW)
    if town == "Ужгород":
        if resp8.status_code == 200:
            soup = BeautifulSoup(resp8.text, features="html.parser")
            soup_list = soup.find_all("div", {"class": "weather-detail__main-panel-left"})
            res8 = soup_list[0].find("div")
            label3 = Label(text=f"Темперетура: {str(res8.text)} °C", font="Arial 18")
            label3.grid(row=3, column=0, padx=10, pady=10, sticky=NW)
            soup_list = soup.find_all("div", {"class": "weather-detail__extra-item"})
            op = soup_list[0].find("div", {"data-key": "fallout"})
            label4 = Label(text=f"Імовірність опадів: {str(op.text)}", font="Arial 19")
            label4.grid(row=4, column=0, padx=10, pady=10, sticky=NW)
    if town == "Вінниця":
        if resp10.status_code == 200:
            soup = BeautifulSoup(resp10.text, features="html.parser")
            soup_list = soup.find_all("div", {"class": "weather-detail__main-panel-left"})
            res10 = soup_list[0].find("div")
            label3 = Label(text=f"Темперетура: {str(res10.text)} °C", font="Arial 18")
            label3.grid(row=3, column=0, padx=10, pady=10, sticky=NW)
            soup_list = soup.find_all("div", {"class": "weather-detail__extra-item"})
            op = soup_list[0].find("div", {"data-key": "fallout"})
            label4 = Label(text=f"Імовірність опадів: {str(op.text)}", font="Arial 19")
            label4.grid(row=4, column=0, padx=10, pady=10, sticky=NW)


list_city = [
    "Київ", "Чернігів", "Суми", "Житомир", "Луцьк", "Рівне", "Львів",
    "Івано-Франківськ", "Ужгород", "Вінниця"
]

root = Tk()
root.geometry("400x600")
root.title("Weather")

label1 = Label(text=f"Дата: {current_time.strftime('%d-%m-%y %I:%M')}", font="Arial 18")
label1.grid(row=0, column=0, padx=10, pady=10, sticky=NW)

label2 = Label(text="Оберіть місто: ", font="Arial 18")
label2.grid(row=1, column=0, padx=10, pady=10, sticky=NW)

box = Combobox(root, values=list_city)
box.grid(row=1, column=0, padx=200, pady=0)

btn = Button(text="Дізнатися погоду", width=15, height=1, font="Arial 14", command=weather)
btn.grid(row=2, column=0, padx=10, pady=10, sticky=W)



root.mainloop()
