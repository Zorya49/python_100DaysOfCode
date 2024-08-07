class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, flight_date, return_date, stop_overs=0, via_city="", via_city_return=""):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.flight_date = flight_date
        self.return_date = return_date
        self.stop_overs = stop_overs
        self.via_city = via_city
        self.via_city_return = via_city_return


