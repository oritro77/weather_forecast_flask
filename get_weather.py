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
        forecast_weather = requests.get(url=full_url)
        return forecast_weather.json()


