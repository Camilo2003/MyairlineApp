import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from entities.airline import Airline  # Import the Airline class

# Create the AirlineApp class


width_button = 22


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


if __name__ == "__main__":
    root = tk.Tk()
    app = AirlineApp(root)
    root.mainloop()
