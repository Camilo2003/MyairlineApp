import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from entities.airline import Airline  # Import the Airline class

# Create the AirlineApp class


width_button = 25


class AirlineApp:
    # Constructor
    def __init__(self, root):
        self.root = root  # Root window
        self.root.title("Airline Management System")
        self.root.geometry("300x500")
        self.airline = Airline()  # Create an instance of the Airline class
        self.create_main_window()  # Call the create_main_window method

    # This method creates the main window
    def create_main_window(self):
        # Create the title label
        self.label_title = ttk.Label(
            self.root, text="Airline Management System", font=("Arial", 15), justify="center")
        self.label_title.pack(pady=10)
        # Create the buttons
        self.button_create_airplane = ttk.Button(
            self.root, text="Create Airplane", command=self.open_create_airplane, width=width_button)
        self.button_create_airplane.pack(pady=10)

        self.button_create_flight = ttk.Button(
            self.root, text="Create Flight", command=self.open_create_flight, width=width_button)
        self.button_create_flight.pack(pady=10)

        self.button_add_passenger = ttk.Button(
            self.root, text="Add Passenger", command=self.open_add_passenger, width=width_button)
        self.button_add_passenger.pack(pady=10)

        self.button_see_airplanes = ttk.Button(
            self.root, text="See Airplanes", command=self.open_see_airplanes, width=width_button)
        self.button_see_airplanes.pack(pady=10)

        self.button_see_flights = ttk.Button(
            self.root, text="See Flights", command=self.open_see_flights, width=width_button)
        self.button_see_flights.pack(pady=10)

        self.button_see_passengers = ttk.Button(
            self.root, text="See Passengers", command=self.open_see_passengers, width=width_button)
        self.button_see_passengers.pack(pady=10)

        self.button_see_passengers_on_flight = ttk.Button(
            self.root, text="Search passengers by flight", command=self.open_search_passengers_by_flight, width=width_button)
        self.button_see_passengers_on_flight.pack(pady=10)

        self.button_change_status_flight = ttk.Button(
            self.root, text="Change status flight", command=self.open_change_status_flight, width=width_button)
        self.button_change_status_flight.pack(pady=10)
    # This method opens the create airplane window

    def open_create_airplane(self):
        # Create the create airplane window
        self.create_airplane_window = tk.Toplevel(self.root)
        self.create_airplane_window.title("Create Airplane")

        # Create the labels and entries
        self.label_airplane_id = ttk.Label(
            self.create_airplane_window, text="ID")
        self.label_airplane_id.grid(row=0, column=0, padx=10, pady=10)
        self.entry_airplane_id = ttk.Entry(self.create_airplane_window)
        self.entry_airplane_id.grid(row=0, column=1, padx=10, pady=10)

        self.label_airplane_brand = ttk.Label(
            self.create_airplane_window, text="Brand")
        self.label_airplane_brand.grid(row=1, column=0, padx=10, pady=10)
        self.entry_airplane_brand = ttk.Entry(self.create_airplane_window)
        self.entry_airplane_brand.grid(row=1, column=1, padx=10, pady=10)

        self.label_airplane_model = ttk.Label(
            self.create_airplane_window, text="Model")
        self.label_airplane_model.grid(row=2, column=0, padx=10, pady=10)
        self.entry_airplane_model = ttk.Entry(self.create_airplane_window)
        self.entry_airplane_model.grid(row=2, column=1, padx=10, pady=10)

        self.label_airplane_capacity = ttk.Label(
            self.create_airplane_window, text="Passenger Capacity")
        self.label_airplane_capacity.grid(row=3, column=0, padx=10, pady=10)
        self.entry_airplane_capacity = ttk.Entry(self.create_airplane_window)
        self.entry_airplane_capacity.grid(row=3, column=1, padx=10, pady=10)

        self.button_create_airplane = ttk.Button(
            self.create_airplane_window, text="Create Airplane", command=self.create_airplane)
        self.button_create_airplane.grid(
            row=4, column=0, columnspan=2, pady=10)

    # This method creates an airplane
    def create_airplane(self):
        try:
            # Get the values from the entries
            id = int(self.entry_airplane_id.get())
            brand = self.entry_airplane_brand.get()
            model = self.entry_airplane_model.get()
            passenger_capacity = int(self.entry_airplane_capacity.get())
            # Call the create_airplane method from the Airline class
            self.airline.create_airplane(id, brand, model, passenger_capacity)
            messagebox.showinfo("Success", "Airplane created successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    # This method opens the create flight window

    def open_create_flight(self):
        # Create the create flight window
        self.create_flight_window = tk.Toplevel(self.root)
        self.create_flight_window.title("Create Flight")

        # Create the labels and entries
        self.label_flight_id = ttk.Label(
            self.create_flight_window, text="Flight ID")
        self.label_flight_id.grid(row=0, column=0, padx=10, pady=10)
        self.entry_flight_id = ttk.Entry(self.create_flight_window)
        self.entry_flight_id.grid(row=0, column=1, padx=10, pady=10)

        self.label_flight_origin = ttk.Label(
            self.create_flight_window, text="Origin")
        self.label_flight_origin.grid(row=1, column=0, padx=10, pady=10)
        self.entry_flight_origin = ttk.Entry(self.create_flight_window)
        self.entry_flight_origin.grid(row=1, column=1, padx=10, pady=10)

        self.label_flight_destination = ttk.Label(
            self.create_flight_window, text="Destination")
        self.label_flight_destination.grid(row=2, column=0, padx=10, pady=10)
        self.entry_flight_destination = ttk.Entry(self.create_flight_window)
        self.entry_flight_destination.grid(row=2, column=1, padx=10, pady=10)

        self.label_flight_departure = ttk.Label(
            self.create_flight_window, text="Departure Time")
        self.label_flight_departure.grid(row=3, column=0, padx=10, pady=10)
        self.entry_flight_departure = ttk.Entry(self.create_flight_window)
        self.entry_flight_departure.grid(row=3, column=1, padx=10, pady=10)

        self.label_flight_arrival = ttk.Label(
            self.create_flight_window, text="Arrival Time")
        self.label_flight_arrival.grid(row=4, column=0, padx=10, pady=10)
        self.entry_flight_arrival = ttk.Entry(self.create_flight_window)
        self.entry_flight_arrival.grid(row=4, column=1, padx=10, pady=10)

        self.label_flight_airplane_id = ttk.Label(
            self.create_flight_window, text="Airplane ID")
        self.label_flight_airplane_id.grid(row=5, column=0, padx=10, pady=10)
        self.entry_flight_airplane_id = ttk.Entry(self.create_flight_window)
        self.entry_flight_airplane_id.grid(row=5, column=1, padx=10, pady=10)

        self.button_create_flight = ttk.Button(
            self.create_flight_window, text="Create Flight", command=self.create_flight)
        self.button_create_flight.grid(row=6, column=0, columnspan=2, pady=10)

    # This method creates a flight
    def create_flight(self):
        try:
            # Get the values from the entries
            id = int(self.entry_flight_id.get())
            origin = self.entry_flight_origin.get()
            destination = self.entry_flight_destination.get()
            departure_time = self.entry_flight_departure.get()
            arrival_time = self.entry_flight_arrival.get()
            airplane_id = int(self.entry_flight_airplane_id.get())
            # Call the create_flight method from the Airline class
            self.airline.create_flight(
                id, origin, destination, departure_time, arrival_time, airplane_id)
            messagebox.showinfo("Success", "Flight created successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    # This method opens the add passenger window
    def open_add_passenger(self):
        # Create the add passenger window
        self.add_passenger_window = tk.Toplevel(self.root)
        self.add_passenger_window.title("Add Passenger")

        # Create the labels and entries
        self.label_passenger_document = ttk.Label(
            self.add_passenger_window, text="Document")
        self.label_passenger_document.grid(row=0, column=0, padx=10, pady=10)
        self.entry_passenger_document = ttk.Entry(self.add_passenger_window)
        self.entry_passenger_document.grid(row=0, column=1, padx=10, pady=10)

        self.label_passenger_first_name = ttk.Label(
            self.add_passenger_window, text="First Name")
        self.label_passenger_first_name.grid(row=1, column=0, padx=10, pady=10)
        self.entry_passenger_first_name = ttk.Entry(self.add_passenger_window)
        self.entry_passenger_first_name.grid(row=1, column=1, padx=10, pady=10)

        self.label_passenger_last_name = ttk.Label(
            self.add_passenger_window, text="Last Name")
        self.label_passenger_last_name.grid(row=2, column=0, padx=10, pady=10)
        self.entry_passenger_last_name = ttk.Entry(self.add_passenger_window)
        self.entry_passenger_last_name.grid(row=2, column=1, padx=10, pady=10)

        self.label_passenger_flight_id = ttk.Label(
            self.add_passenger_window, text="Flight ID")
        self.label_passenger_flight_id.grid(row=3, column=0, padx=10, pady=10)
        self.entry_passenger_flight_id = ttk.Entry(self.add_passenger_window)
        self.entry_passenger_flight_id.grid(row=3, column=1, padx=10, pady=10)

        self.button_create_passenger = ttk.Button(
            self.add_passenger_window, text="Add Passenger", command=self.create_passenger)
        self.button_create_passenger.grid(
            row=4, column=0, columnspan=2, pady=10)

    # This method creates a passenger
    def create_passenger(self):
        try:
            # Get the values from the entries
            document = int(self.entry_passenger_document.get())
            first_name = self.entry_passenger_first_name.get()
            last_name = self.entry_passenger_last_name.get()
            id_flight = int(self.entry_passenger_flight_id.get())
            # Call the create_passenger method from the Airline class
            self.airline.create_passenger(
                document, first_name, last_name, id_flight)
            messagebox.showinfo("Success", "Passenger created successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    # This method opens the see airplanes window
    def open_see_airplanes(self):
        # Create the see airplanes window
        self.see_airplanes_window = tk.Toplevel(self.root)
        self.see_airplanes_window.title("See Airplanes")

        # Call the get_airplanes method from the Airline class
        airplanes = self.airline.get_airplanes()
        if airplanes:
            for airplane in airplanes:
                airplane_info = airplane.get_info()
                label_airplane_info = ttk.Label(
                    self.see_airplanes_window, text=airplane_info, font=("Arial", 10))
                label_airplane_info.pack(pady=10)
        else:
            label_no_airplanes = ttk.Label(
                self.see_airplanes_window, text="No airplanes found.")
            label_no_airplanes.pack()

    # This method opens the see flights window
    def open_see_flights(self):
        # Create the see flights window
        self.see_flights_window = tk.Toplevel(self.root)
        self.see_flights_window.title("See Flights")

        # Call the get_flights method from the Airline class
        flights = self.airline.get_flights()
        if flights:
            for flight in flights:
                flight_info = flight.get_info()
                label_flight_info = ttk.Label(
                    self.see_flights_window, text=flight_info, font=("Arial", 10))
                label_flight_info.pack(pady=10)
        else:
            label_no_flights = ttk.Label(
                self.see_flights_window, text="No flights found.")
            label_no_flights.pack()

    # This method opens the see passengers window
    def open_see_passengers(self):
        # Create the see passengers window
        self.see_passengers_window = tk.Toplevel(self.root)
        self.see_passengers_window.title("See Passengers")

        # Call the get_passengers method from the Airline class
        passengers = self.airline.get_passengers()
        if passengers:
            for passenger in passengers:
                passenger_info = passenger.get_info()
                label_passenger_info = ttk.Label(
                    self.see_passengers_window, text=passenger_info, font=("Arial", 10))
                label_passenger_info.pack(pady=10)
        else:
            label_no_passengers = ttk.Label(
                self.see_passengers_window, text="No passengers found.")
            label_no_passengers.pack()

        def open_see_passengers_by_flight(self):
            # Create the see passengers by flight window
            self.see_passengers_by_flight_window = tk.Toplevel(self.root)
            self.see_passengers_by_flight_window.title(
                "See Passengers by Flight")

            # Create the labels and entries
            self.label_flight_id = ttk.Label(
                self.see_passengers_by_flight_window, text="Flight ID")
            self.label_flight_id.grid(row=0, column=0, padx=10, pady=10)
            self.entry_flight_id = ttk.Entry(
                self.see_passengers_by_flight_window)
            self.entry_flight_id.grid(row=0, column=1, padx=10, pady=10)

            self.button_see_passengers = ttk.Button(
                self.see_passengers_by_flight_window, text="See Passengers", command=self.see_passengers_by_flight)
            self.button_see_passengers.grid(
                row=1, column=0, columnspan=2, pady=10)

    # This method opens the see passengers by flight window
    def open_search_passengers_by_flight(self):
        # Create the search passengers by flight window
        self.search_passengers_by_flight_window = tk.Toplevel(self.root)
        self.search_passengers_by_flight_window.title(
            "Search Passengers by Flight")

        # Create the labels and entries
        self.label_flight_id = ttk.Label(
            self.search_passengers_by_flight_window, text="Flight ID")
        self.label_flight_id.grid(row=0, column=0, padx=10, pady=10)
        self.entry_flight_id = ttk.Entry(
            self.search_passengers_by_flight_window)
        self.entry_flight_id.grid(row=0, column=1, padx=10, pady=10)

        self.button_search_passengers = ttk.Button(
            self.search_passengers_by_flight_window, text="Search Passengers", command=self.search_passengers_by_flight)
        self.button_search_passengers.grid(
            row=1, column=0, columnspan=2, pady=10)

    # This method searches passengers by flight
    def search_passengers_by_flight(self):
        try:
            # Get the value from the entry
            flight_id = int(self.entry_flight_id.get())
            # Call the get_passengers_by_flight method from the Airline class
            passengers = self.airline.get_passengers_by_flight(flight_id)
            if passengers:
                # Create the see passengers by flight window
                self.see_passengers_by_flight_window = tk.Toplevel(
                    self.root)
                self.see_passengers_by_flight_window.title(
                    "Passengers on Flight")

                for passenger in passengers:
                    passenger_info = passenger.get_info()
                    label_passenger_info = ttk.Label(
                        self.see_passengers_by_flight_window, text=passenger_info, font=("Arial", 10))
                    label_passenger_info.pack(pady=10)
            else:
                messagebox.showinfo("Success", "No passengers found.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def open_change_status_flight(self):
        # Create the change status flight window
        self.change_status_flight_window = tk.Toplevel(self.root)
        self.change_status_flight_window.title("Change Status Flight")

        # Create the labels and comboboxes
        self.label_flight_id = ttk.Label(
            self.change_status_flight_window, text="Flight ID")
        self.label_flight_id.grid(row=0, column=0, padx=10, pady=10)
        self.entry_flight_id = ttk.Entry(self.change_status_flight_window)
        self.entry_flight_id.grid(row=0, column=1, padx=10, pady=10)

        # Create the combobox for the status
        self.label_flight_status = ttk.Label(
            self.change_status_flight_window, text="Status")
        self.label_flight_status.grid(row=1, column=0, padx=10, pady=10)
        self.option_flight_status = ttk.Combobox(
            self.change_status_flight_window, values=["Scheduled", "Delayed", "Cancelled", "Finished"])
        self.option_flight_status.grid(row=1, column=1, padx=10, pady=10)

        # Set the initial selection for the combobox
        self.option_flight_status.set("Scheduled")

        self.button_change_status = ttk.Button(
            self.change_status_flight_window, text="Change Status", command=self.change_status_flight)
        self.button_change_status.grid(row=2, column=0, columnspan=2, pady=10)

    # This method changes the status of a flight
    def change_status_flight(self):
        try:
            # Get the values from the entries
            id = int(self.entry_flight_id.get())
            status = self.option_flight_status.get()
            # Call the change_status_flight method from the Airline class
            self.airline.change_status_flight(id, status)
            messagebox.showinfo("Success", "Status changed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = AirlineApp(root)
    root.mainloop()

    # # Initial example
    # airline = Airline()
    # airline.create_airplane(1, "Boeing", "747", 416)
    # airline.create_airplane(2, "Airbus", "A380", 853)
    # airline.create_airplane(3, "Boeing", "777", 550)

    # airline.create_flight(11001, "Bogota", "Barranquilla",
    #                       "2021-10-10 06:00", "2021-10-10 07:00", 1)
    # airline.create_flight(11002, "Bogota", "Bucaramanga",
    #                       "2021-10-10 08:00", "2021-10-10 09:00", 2)
    # airline.create_flight(11003, "Bogota", "Medellin",
    #                       "2021-10-10 10:00", "2021-10-10 11:00", 1)
    # airline.create_flight(11004, "Bogota", "Cali",
    #                       "2021-10-10 12:00", "2021-10-10 13:00", 2)
    # airline.create_flight(11005, "Bogota", "Cartagena",
    #                       "2021-10-10 14:00", "2021-10-10 15:00", 1)
    # airline.create_flight(11006, "Bogota", "Santa Marta",
    #                       "2021-10-10 16:00", "2021-10-10 17:00", 2)
    # airline.create_flight(11007, "Pereira", "Miami",
    #                       "2021-11-5 18:00", " 2021-11-5 16:00", 3)

    # airline.create_passenger(888001, "Juan", "Perez", 11001)
    # airline.create_passenger(888002, "Maria", "Gomez", 11002)
    # airline.create_passenger(888003, "Luis", "Gonzales", 11003)
    # airline.create_passenger(888004, "Mario", "Felipe", 11004)
    # airline.create_passenger(888005, "Alex", "Smith", 11005)
    # airline.create_passenger(888006, "Jhon", "Doe", 11006)
    # airline.create_passenger(888007, "Juana", "Pancha", 11007)
    # airline.create_passenger(888008, "Maria", "Sanchez", 11001)
    # airline.create_passenger(888009, "Alfredo", "Gutierrez", 11002)
    # airline.create_passenger(888010, "Luisa", "Gomez", 11003)
    # airline.create_passenger(888011, "Marlos", "Moreno", 11004)
