# Creation class Flight


# Importing necessary classes
from Airplane import Airplane
from Passenger import Passenger

# Flight class


class Flight:
    def __init__(self, id: int, airplane: Airplane, passengers: list[Passenger], departure: str, destination: str, departure_time: str, arrival_time: str, is_finished=False) -> None:
        self.__id = id
        self.__airplane = airplane
        self.__passengers = passengers
        self.__departure = departure
        self.__destination = destination
        self.__departure_time = departure_time
        self.__arrival_time = arrival_time
        self.__is_finished = is_finished

    # Getters
    def get_id(self):
        return self.__id

    def get_airplane(self):
        return self.__airplane

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

    def is_finished(self):
        return self.__is_finished

    # Setters
    def set_id(self, id):
        self.__id = id

    def set_airplane(self, airplane):
        self.__airplane = airplane

    def set_departure(self, departure):
        self.__departure = departure

    def set_destination(self, destination):
        self.__destination = destination

    def set_departure_time(self, departure_time):
        self.__departure_time = departure_time

    def set_arrival_time(self, arrival_time):
        self.__arrival_time = arrival_time

    def set_is_finished_true(self):
        self.__is_finished = True

    def set_is_finished_false(self):
        self.__is_finished = False

    # Methods
    def add_passenger(self, passenger):
        self.__passengers.append(passenger)

    def remove_passenger(self, id_passenger: int):
        self.__passengers = [
            passenger for passenger in self.__passengers if passenger.get_id() != id_passenger]

    def get_info(self):
        return f"Flight ID: {self.__id}, Departure: {self.__departure}, Destination: {self.__destination}, Departure Time: {self.__departure_time}, Arrival Time: {self.__arrival_time}, Finished: {self.__is_finished}"

    def get_passengers_info(self):
        list_info_passengers = []
        for passenger in self.__passengers:
            list_info_passengers.append(passenger.get_info())
        return list_info_passengers


# Example
# Airplane
Airplane1 = Airplane(1, "Boeing", "747", 416)
Airplane2 = Airplane(2, "Airbus", "A380", 853)

# Passengers
Passenger1 = Passenger(1, "John", "Doe", 1, 1)
Passenger2 = Passenger(2, "Jane", "Doe", 1, 2)
Passenger3 = Passenger(3, "Alice", "Doe", 2, 1)
Passenger4 = Passenger(4, "Bob", "Doe", 2, 2)

# Flight
Flight1 = Flight(1, Airplane1, [],
                 "New York", "Los Angeles", "08:00", "10:00")
Flight2 = Flight(2, Airplane2, [],
                 "Paris", "Tokyo", "12:00", "20:00")


# Adding passengers to the flight
Flight1.add_passenger(Passenger1)
Flight1.add_passenger(Passenger2)
Flight2.add_passenger(Passenger3)
Flight2.add_passenger(Passenger4)

# Getting passengers info
list_passengers_info = Flight1.get_passengers_info()
print(list_passengers_info)
