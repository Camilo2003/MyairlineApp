# Creation class Flight


# Importing necessary classes
from entities.passenger import Passenger

# Flight class


class Flight:
    def __init__(self, id: int, id_airplane: int, passengers: list[Passenger], departure: str, destination: str, departure_time: str, arrival_time: str, status: str) -> None:
        self.__id = int(id)
        self.__id_airplane = int(id_airplane)
        self.__passengers = passengers
        self.__departure = departure
        self.__destination = destination
        self.__departure_time = departure_time
        self.__arrival_time = arrival_time
        self.__status = status

    # Getters
    def get_id(self):
        return self.__id

    def get_id_airplane(self):
        return self.__id_airplane

    def get_passengers(self):
        return self.__passengers

    def get_departure(self):
        return self.__departure

    def get_destination(self):
        return self.__destination

    def get_departure_time(self):
        return self.__departure_time

    def get_arrival_time(self):
        return self.__arrival_time

    def get_status(self):
        return self.__status

    # Setters
    def set_id(self, id):
        self.__id = int(id)

    def set_id_airplane(self, id_airplane):
        self.__id_airplane = int(id_airplane)

    def set_departure(self, departure):
        self.__departure = departure

    def set_destination(self, destination):
        self.__destination = destination

    def set_departure_time(self, departure_time):
        self.__departure_time = departure_time

    def set_arrival_time(self, arrival_time):
        self.__arrival_time = arrival_time

    def set_status(self, status):
        self.__status = status

    # Methods
    def add_passenger(self, passenger):
        self.__passengers.append(passenger)

    def remove_passenger(self, id_passenger: int):
        for passenger in self.__passengers:
            if passenger.get_id() == id_passenger:
                self.__passengers.remove(passenger)

    def get_info(self):
        return f"ID: {self.__id}, ID Airplane: {self.__id_airplane}, Departure: {self.__departure}, Destination: {self.__destination}, Departure Time: {self.__departure_time}, Arrival Time: {self.__arrival_time}, Status: {self.__status}"

    def get_passengers_info(self):
        list_info_passengers = []
        for passenger in self.__passengers:
            list_info_passengers.append(passenger.get_info())
        return list_info_passengers
