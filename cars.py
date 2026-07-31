class cars:
    def __init__(self, number, name, age, car_type, team,speed, capacity):
        self.__number = number
        self.__name = name
        self.__age = age
        self.__car_type = car_type
        self.__team = team
        self.__speed = speed
        self.__capacity = capacity
    
    def set_number(self, number):
        self.__number = number
        
    def set_name(self, name):
        self.__name = name
    
    def set_age(self, age): 
        self.__age = age
    
    def set_car_type(self, car_type):
        self.__car_type = car_type
    
    def set_team(self, team):
        self.__team = team
        
    def set_speed(self, speed):
        self.__speed = speed  
        
    def set_capacity(self, capacity):
        self.__capacity = capacity    
    
    def get_number(self):
        return self.__number  
    
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_car_type(self):
        return self.__car_type

    def get_team(self):
        return self.__team

    def get_speed(self):
        return self.__speed

    def get_capacity(self):
        return self.__capacity
    
    def display(self):
        print("Car Number:", self.__number)
        print("Car Name:", self.__name)
        print("Car Age:", self.__age)
        print("Car Type:", self.__car_type)
        print("Car Team:", self.__team)
        print("Car Speed:", self.__speed)
        print("Car Capacity:", self.__capacity)
        
    def calculate_performance(self):
        raise NotImplementedError