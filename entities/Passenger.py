
# Importing necessary person class
from Person import Person


# Creation of the Passenger class


# Passenger class
# Inheritance from Person class
class Passenger(Person):
    def __init__(self, document: int, first_name: str, last_name: str, id_flight: int) -> None:
        super().__init__(document, first_name, last_name)
        self.__id_flight = id_flight

    # Getters
    def get_id_flight(self):
        return self.__id_flight

    # Setters
    def set_id_flight(self, id_flight):
        self.__id_flight = id_flight

    # Methods
    def get_info(self):
        return f"{super().get_info()}, ID Flight: {self.__id_flight}"
