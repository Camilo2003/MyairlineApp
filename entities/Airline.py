# Creation class Airline

# Airline class

class Airline:
    def __init__(self, name: str, airplanes: list, passengers: list) -> None:
        self.__name = name
        self.__airplanes = airplanes
        self.__passengers = passengers

    # Getters
    def get_name(self):
        return self.__name

    def get_airplanes(self):
        return self.__airplanes

    def get_passengers(self):
        return self.__passengers

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_airplanes(self, airplanes):
        self.__airplanes = airplanes

    def set_passengers(self, passengers):
        self.__passengers = passengers

    # Methods
    def add_airplane(self, airplane):
        self.__airplanes.append(airplane)

    def add_passenger(self, passenger):
        self.__passengers.append(passenger)

    def get_info(self):
        return f"Airline Name: {self.__name}, Airplanes: {len(self.__airplanes)}, Passengers: {len(self.__passengers)}"

    def get_info_and_status(self):
        return f"Airline Name: {self.__name}, Airplanes: {len(self.__airplanes)}, Passengers: {len(self.__passengers)}"

    def get_info_airplanes(self):
        return [airplane.get_info_and_status() for airplane in self.__airplanes]

    def get_info_passengers(self):
        return [passenger.get_info() for passenger in self.__passengers]
