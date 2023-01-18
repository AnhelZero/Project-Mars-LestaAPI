from fastapi import FastAPI
import requests

app = FastAPI()

# Укажите нацию/id танка для поиска
variable = "57937"
# Выберите vehicles или vehicleprofile (работает только с поиском по id)
selects = "vehicles"
# Выберите поиск по нации (nation) или id (tank_id)
search = "tank_id"
# Ключ доступа API
key = "214c61dc71b81996bedc15084ef9673f"

# Поиск техники в базе данных Lesta
response = requests.get(
url=f'https://api.tanki.su/wot/encyclopedia/{selects}/?application_id={key}&{search}={variable}',
)
# Просматриваем значения атрибутов результатов поиска по базе Lesta
json_response = response.json()

#print(response.json())

@app.get ('/')
def home():
    return response.json()
