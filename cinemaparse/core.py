#CinemaParser
class CinemaParser:
    def __init__(self, city = "Msk"):
        if isinstance(city,str) == True:
            self.city = city
        else:
            raise TypeError("Not str")
CinemaParser("Spb")
