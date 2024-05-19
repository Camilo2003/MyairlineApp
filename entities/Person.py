
# Creation of the Person class

# Person class
class Person:
    def __init__(self, document: int, first_name: str, last_name: str) -> None:
        self.__document = document
        self.__first_name = first_name
        self.__last_name = last_name

# Getters
    def get_document(self):
        return self.__document

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

# Setters
    def set_document(self, document):
        self.__document = document

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

# Methods
    def get_info(self):
        return f"Document: {self.__document}, First Name: {self.__first_name}, Last Name: {self.__last_name}"


# # example
# person1 = Person(123456789, "John", "Doe")
# print(person1.get_info())
