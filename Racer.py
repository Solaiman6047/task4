from Car import Car

class Racer(Car):
    def __init__(self, number, name, age, car_type, team, speed, capacity, races, laps):
        super().__init__(number, name, age, car_type, team, speed, capacity)
        self.__races = races
        self.__laps = laps
        self.__performance = self.calculate_performance()
        
    def set_races(self, races):
        self.__races = races

    def set_laps(self, laps):
        self.__laps = laps

    def get_races(self):
        return self.__races

    def get_laps(self):
        return self.__laps  
    
    def calculate_performance(self):
        perfomance = (self.get_speed() * 10) + self.get_capacity()
        return perfomance
    
    def display(self):
        super().display()
        print("Number of Races:", self.__races)
        print("Number of Laps:", self.__laps)   
