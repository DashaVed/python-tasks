import requests
import bs4

response = requests.get("https://ru-meteo.ru/")

tree = bs4.BeautifulSoup(response.text, 'html.parser')

for item in tree.select(".pgname"):
    print(item.text)

print("Погода сегодня:", tree.select('.current-temp')[0].text)

print("Погода на неделю")

item = tree.select('#forecast')[0]
days = item.select('.dt')
weather_per_day = item.select(".wtr")

if len(days) != len(weather_per_day):
    print("Не удалось получить погоду на неделю")
else:
    for i in range(len(days)):
        print(days[i].text, weather_per_day[i].text)
