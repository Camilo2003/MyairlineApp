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

    # This method creates a new airplane and writes it to the airplanes.txt file.
    def create_airplane(self, id: int, brand: str, model: str, passenger_capacity: int) -> None:
        airplane = Airplane(id, brand, model, passenger_capacity)
        try:
            with open("airplanes.txt", "a") as file:
                file.write(f"{airplane.get_info()}\n")
        except Exception as e:
            print(f"An error occurred: {e}")

    # This method gets the airplanes from the airplanes.txt file and add them to the airplanes list, and then returns the airplane list.
    def get_airplanes(self):
        try:
            with open("airplanes.txt", "r") as file:
                for line in file:
                    line = line.strip().split(", ")
                    line = [i.split(": ")[1] for i in line]
                    # print(line)
                    airplane = Airplane(
                        line[0], line[1], line[2], line[3], line[4])
                    # print(airplane.get_info())
                    self.__airplanes_list.append(airplane)
            return self.__airplanes_list
        except Exception as e:
            print(f"An error occurred: {e}")

    # This method receives an airplane id and returns the airplane object if it exists in the airplanes list.
    def get_airplane_by_id(self, id: int) -> Airplane:
        self.get_airplanes()
        for airplane in self.__airplanes_list:
            if airplane.get_id() == id:
                # print(airplane.get_info())
                return airplane
        return None

    def create_flight(self, id: int, origin: str, destination: str, departure_time: str, arrival_time: str, airplane_id: int) -> None:
        airplane = self.get_airplane_by_id(airplane_id)
        if airplane:
            flight = Flight(id, origin, destination, departure_time,
                            arrival_time, airplane)
            try:
                with open("flights.txt", "a") as file:
                    file.write(f"{flight.get_info()}\n")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Airplane not found")


airline = Airline()

# airline.create_airplane(1, "Boeing", "747", 416)
# airline.create_airplane(2, "Airbus", "A380", 853)
airplane = airline.get_airplane_by_id(1)
print(airplane.get_info())
