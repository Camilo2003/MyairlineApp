# This file contains the Airline class, which will manage the flights, airplanes, and passengers of an unique airline.

# import Airplane
from airplane import Airplane

# import Flight
from flight import Flight

# import Passenger
from passenger import Passenger


# Creation class Airline
# This class will manage the flights, airplanes, and passengers of an unique airline.
# Airline class

# Singleton pattern
class SingletonMeta(type):
    """
    Meta clase para implementar el patrón Singleton.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Airline(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.__flights_list = []
        self.__airplanes_list = []
        self.__passengers_list = []

    def create_airplane(self, id: int, brand: str, model: str, passenger_capacity: int) -> None:
        airplane = Airplane(id, brand, model, passenger_capacity)
        try:
            with open("airplanes.txt", "a") as file:
                file.write(f"{airplane.get_info()}\n")
        except Exception as e:
            print(f"An error occurred: {e}")


airline = Airline()

airline.create_airplane(1, "Boeing", "747", 416)
airline.create_airplane(2, "Airbus", "A380", 853)
