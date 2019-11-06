#CinemaParser
class CinemaParser:
    def __init__(self, city = "Msk"):
        if isinstance(city,str) == True:
            self.city = city
        else:
            raise TypeError("Not str")
CinemaParser("Spb")



#CinemaParser
import requests as re
class CinemaParser:
    def __init__(self, city = "Msk"):
        if isinstance(city,str) == True:
            self.city = city
        else:
            raise TypeError("Not str")
    def extract_raw_content():
        if self.city == "Msk":
            self.content = re.get("https://msk.subscity.ru")
CinemaParser()
