import requests
from flask import Flask, jsonify

EXCHANGE_URL = 'https://openexchangerates.org/api/latest.json?app_id=2bcdbe4082624c738ac1bf703f51e054'
EXCHANGE_PARAMS = {'symbols': 'RUB,EUR,UZS'}

WEATHER_URL = 'http://api.weatherstack.com/current?access_key=7d66abecd15f506f55bcabe1e729bfec'
WEATHER_PARAMS={'query': 'Cape Town'}

WEATHER_PARAMSMY={'query': 'Tashkent'}

app = Flask(__name__)

@app.route('/get',methods=['GET'])
def get():
    exchange_data = requests.get(EXCHANGE_URL, EXCHANGE_PARAMS)
    weather_my_city = requests.get(WEATHER_URL, WEATHER_PARAMSMY)

    return jsonify({
        'kurs_dollar': exchange_data.json()['rates'],
        'Toshkentda_harorat': weather_my_city.json()['current']['temperature']
    })

if __name__ == "__main__":
    app.run()

