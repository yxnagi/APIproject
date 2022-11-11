import logging
from APIproject.core.utils import get_url


log = logging.getLogger(__name__)

class weather:

    arrayoptions = ["rain", "visibility"]

    def __init__(self):
        log.info("LOADED WEATHER")
        self.url = f"https://api.open-meteo.com/v1/forecast"



    def sortoption(self, options:str):
        optionslist = list(options.split(","))
        for x in optionslist:
            if x in self.arrayoptions:
                new_url = new_url + f",{x}"




    def get_weather(self, longitude:float, latitude:float, rain:bool):
          new_url = f"{self.url}?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
          if rain == True:
              new_url = new_url+f",rain"
              log.info(f"RAIN HAS BEEN REQUESTED")
          log.info(new_url)
          weather_data = get_url(new_url)
          return weather_data
