from Car import Car

class SupportVehicle(Car):
    def __init__(self, number, name, age, car_type, team, speed, capacity,crew_size, reliability_rating ):
        super().__init__(number, name, age, car_type, team, speed, capacity)
        self.__crew_size = crew_size
        self.__reliability_rating = reliability_rating
        self.__performance = self.calculate_performance()

    def set_crew_size(self, crew_size):
        self.__crew_size = crew_size

    def set_reliability_rating(self, reliability_rating):
        self.__reliability_rating = reliability_rating

    def get_crew_size(self):
        return self.__crew_size

    def get_reliability_rating(self):
        return self.__reliability_rating

    def calculate_performance(self):
        perfomance = (self.get_speed() * 5) + (self.get_capacity() *5)
        return perfomance
    
    def display(self):
        super().display()
        print("Crew Size:", self.__crew_size)
        print("Reliability Rating:", self.__reliability_rating)