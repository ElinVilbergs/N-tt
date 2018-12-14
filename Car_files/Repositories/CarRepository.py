from Models.Car import Car

import csv

class CarRepository:
    
    def __init__(self):
        self.__cars = []

    def add_car(self, car):
        # first add to file then to private list
        with open("./Data/availablecars.csv", "a+", encoding="utf-8", newline="") as cars_file:
            plate = car.get_plate()
            make = car.get_make()
            cars_file.write("{},{}\n".format(plate, make))
            
    def get_cars(self):
        if self.__cars == []:
            with open("./Data/availablecars.csv", "r", encoding="utf-8", newline="") as cars_file:
                for line in cars_file.readlines():
                    plate, make = line.split(",")
                    new_car = Car(plate, make)
                    self.__cars.append(new_car)    
        
        return self.__cars

    def rented(self):
        with open("./Data/rentedcars.csv", "r") as findcustomer:
            findcustomerreader = csv.DictReader(findcustomer)
            for line in findcustomerreader:
                print(line)