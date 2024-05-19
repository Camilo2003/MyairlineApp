
# Creation of the Airplane class

# Airplane class
class Airplane:
    def __init__(self, id: int, brand: str, model: str, passenger_capacity: int, is_on_flight=False) -> None:
        self.__id = int(id)
        self.__brand = brand
        self.__model = model
        self.__passenger_capacity = int(passenger_capacity)
        self.__is_on_flight = is_on_flight

# Getters
    def get_id(self):
        return self.__id

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_passenger_capacity(self):
        return self.__passenger_capacity

    def is_on_flight(self):
        return self.__is_on_flight

# Setters
    def set_id(self, id):
        self.__id = int(id)

    def set_brand(self, brand):
        self.__brand = brand

    def set_model(self, model):
        self.__model = model

    def set_passenger_capacity(self, passenger_capacity):
        self.__passenger_capacity = int(passenger_capacity)

# Methods

    def set_on_flight_true(self):
        self.__is_on_flight = True

    def set_on_flight_false(self):
        self.__is_on_flight = False

    def get_info(self):
        return f"ID: {self.__id}, Brand: {self.__brand}, Model: {self.__model}, Passenger Capacity: {self.__passenger_capacity}, Is on flight: {self.__is_on_flight}"
