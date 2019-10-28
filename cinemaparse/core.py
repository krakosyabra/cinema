class CinemaParser:
    def __init__(self, city = "Moscow"):
        if(type(city) == str):
            self.city = city
        else:
            raise TypeError("Not str")
CinemaParser(1)
