
class flighttickethelper:

    def __init__(self,flight,src,dest,flightdate):
        self.flight = flight
        self.src = src
        self.dest = dest
        self.flightdate = flightdate

    def get_flights(self):
        flights = [
            {"src": "ewr", "dest": "del", "price": 1000, "date": "12/13/2010", "time": "10:20"},
            {"src": "sfo", "dest": "del", "price": 1100, "date": "12/15/2010", "time": "14:50"},
            {"src": "ewr", "dest": "mum", "price": 1324, "date": "12/14/2010", "time": "16:20"},
            {"src": "jfk", "dest": "del", "price": 989, "date": "12/16/2010", "time": "19:20"},
           ]
        return flights