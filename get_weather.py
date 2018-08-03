import requests
import config

class Weather():

    def get_weather_forecast(self, lat, lon, unit='si'):
        """

        :param lat:
        :param lon:
        :return: json data of weather forecast
        """

        full_url = config.DARK_SKY_FORECAST_API + config.DARK_SKY_API_SECRET_KEY + '/' + str(lat) + ',' + str(lon) + '?units='+unit
        print(full_url)
        forecast_weather = requests.get(url=full_url)
        status_code = forecast_weather.status_code
        response_json = forecast_weather.json()
        if status_code == 200:
            return response_json
        else:
            raise response_json["error"]
