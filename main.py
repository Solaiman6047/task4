from Racer import Racer
from SupportVehicle import SupportVehicle
from Car import Car


garage = []

def check_in():
    number = int(input("Enter the number of the car: "))
    for cars in garage:
        if cars.get_number() == number:
            print("Car with this number already exists.")
            return
    name = input("Enter the name of the car: ")
    age = int(input("Enter the age of the car: ")) 
    team = input("Enter the team of the car: ")
    speed = int(input("Enter the speed of the car: "))
    capacity = int(input("Enter the capacity of the car: "))

    car_type = input("Enter the type of the car: ")
    if car_type.lower() == "racer":
        races = int(input("Enter the number of races: "))
        laps = int(input("Enter the number of laps: "))  
        racer = Racer(number, name, age, car_type, team, speed, capacity, races, laps)
        garage.append(racer)
        print("Car checked in successfully.")
    elif car_type.lower() == "support vehicle":
        crew_size = int(input("Enter the crew size: "))
        reliability_rating = float(input("Enter the reliability rating: "))
        support_vehicle = SupportVehicle(number, name, age, car_type, team, speed, capacity, crew_size, reliability_rating)
        garage.append(support_vehicle)
        print("Car checked in successfully.")
    else:
        print("Invalid car type. Please enter either 'Racer' or 'Support Vehicle'.")
        return

def view_garage():
    if not garage:
        print("The garage is empty.")
        return
    print ("Cars in the garage:")
    for cars in garage:
        cars.display()
        print("Performance:", cars.calculate_performance())
        print("--------------------")

def tune_up():
    number = int(input("Enter the number of the car to tune up: "))
    for cars in garage:
        if cars.get_number() == number:
            print("Tuning up the car...")
            new_name= input("Enter the new name: ")
            new_team = input("Enter the new team: ")
            new_age = int(input("Enter the new age: "))
            new_speed = int(input("Enter the new speed: "))
            new_capacity = int(input("Enter the new capacity: "))
            cars.set_name(new_name)
            cars.set_team(new_team)
            cars.set_age(new_age)
            cars.set_speed(new_speed)
            cars.set_capacity(new_capacity)
            if isinstance(cars, Racer):
                new_races = int(input("Enter the new number of races: "))
                new_laps = int(input("Enter the new number of laps: "))   
                cars.set_races(new_races)
                cars.set_laps(new_laps)  
            else:
                new_crew_size = int(input("Enter the new crew size: "))
                new_reliability_rating = float(input("Enter the new reliability rating: ")) 
                cars.set_crew_size(new_crew_size)
                cars.set_reliability_rating(new_reliability_rating)
            print("Updating data...")
            print("Car tuned up successfully.")
            return
    print("Car with this number not found.")

def delete_car():
    number = int(input("Enter the number of the car to delete: "))
    print("Searching for the car...")
    for cars in garage:
        if cars.get_number() == number:
            print("Car found.")
            confirmation = input("Are you sure you want to delete this car? (yes/no): ")
            if confirmation.lower() == "yes":
                print("Deleting the car...")
                garage.remove(cars)
                print("Car deleted successfully.")
            return
    print("Car with this number not found.")

def report():
    if not garage:
        print("The garage is empty.")
        return
    print("Garage Report:")
    l = len(garage)
    print("Total number of cars:", l)
    average_performance = sum(cars.calculate_performance() for cars in garage) / l
    print("Average performance of cars:", average_performance)
    teams = {}
    for cars in garage:
        team = cars.get_team()
        if team in teams:
            teams[team] += 1
        else:
            teams[team] = 1
    print("Teams and their cars:")
    for team, cars in teams.items():
        print("Team:", team)
        print("Cars:", cars)
        
def search_car():
    search_type = input("Search by number or name? (Enter 'number' or 'name'): ")
    if search_type.lower() == "number":
        search_by_number()
    elif search_type.lower() == "name":
        search_by_name()
    else:
        print("Invalid search type. Please enter either 'number' or 'name'.")

def search_by_number():
    number = int(input("Enter the number of the car to search: "))
    for cars in garage:
        if cars.get_number() == number:
            print("Car found:")
            cars.display()
            print("Performance:", cars.calculate_performance())
            return
    print("Car with this number not found.")

def search_by_name():
    name = input("Enter the name of the car to search: ")
    for cars in garage:
        if cars.get_name() == name:
            print("Car found:")
            cars.display()
            print("Performance:", cars.calculate_performance())
            return
    print("Car with this name not found.")
    
def save_garage_to_file():
    data = []
    for cars in garage:
        car_data = {
            "number": cars.get_number(),
            "name": cars.get_name(),
            "age": cars.get_age(),
            "car_type": cars.get_car_type(),
            "team": cars.get_team(),
            "speed": cars.get_speed(),
            "capacity": cars.get_capacity()
        }
        if isinstance(cars, Racer):
            car_data["races"] = cars.get_races()
            car_data["laps"] = cars.get_laps()
        elif isinstance(cars, SupportVehicle):
            car_data["crew_size"] = cars.get_crew_size()
            car_data["reliability_rating"] = cars.get_reliability_rating()
        data.append(car_data)
        with open("garage.json", "w") as file:
            json.dump(data, file, indent=4)

import json
file_path= "garage.json"
try:
    with open(file_path, "r") as file:
        data= json.load(file)
        for car_data in data:
            if isinstance(car_data, Racer):
                car = Racer(car_data["number"], car_data["name"], car_data["age"], car_data["car_type"], car_data["team"], car_data["speed"], car_data["capacity"], car_data["races"], car_data["laps"])
                garage.append(car)
            elif isinstance(car_data, SupportVehicle):
                car = SupportVehicle(car_data["number"], car_data["name"], car_data["age"], car_data["car_type"], car_data["team"], car_data["speed"], car_data["capacity"], car_data["crew_size"], car_data["reliability_rating"])
                garage.append(car)
except FileNotFoundError:
    file = open(file_path, "w") 

while True:
    print("\nGarage Management System")
    print("1. Check-in a car")
    print("2. View garage")
    print("3. Tune-up a car")
    print("4. Delete a car")
    print("5. Report")
    print("6. Search for a car")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        check_in()
    elif choice == "2":
        view_garage()
    elif choice == "3":
        tune_up()
    elif choice == "4":
        delete_car()
    elif choice == "5":
        report()
    elif choice == "6":
        search_car()
    elif choice == "7":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
    save_garage_to_file()