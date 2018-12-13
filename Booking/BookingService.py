from BookingRepository import BookingRepository
from NewBooking import NewBooking

import csv
import os

class BookingService:
    def __init__(self):
        self.__booking_repo = BookingRepository()

    def add_booking(self, booking):
        if self.is_valid_booking(booking):
            self.__booking_repo.add_booking(booking)
    
    def is_valid_booking(self, booking):
        return True

    def get_booking(self):
        return self.__booking_repo.get_booking()

    def get_booking_by_genre(self, genre):
        pass

###### Viðbætur #####

        # action == "1":
            #Add booking
        def booking_menu_1(self):
            balance = 0
            print("Customer needs to be registerd\n")
            ssn = input("Enter customer social security number: ")
            car_category = input("Enter car category: 1,2 or 3: ")
            #Mismunandi flokkar gefa mismunandi verð:
            if car_category == "1":
                fullprice = balance + 12000
            elif car_category == "2":
                fullprice = balance + 23000
            elif car_category == "3":
                fullprice = balance + 50000
            else:
                print("Error")
            
            #Setja inn bílnúmerið hjá þeim bíl sem á að taka frá:
            plate_num = input("Enter car plate number: ")
            
            #Setja í repo fall:
            with open('.availablecars.csv', 'r', encoding="utf-8", newline="") as inp, open('.rentedcars.csv', 'a+', encoding="utf-8", newline="") as out:
                writer = csv.DictWriter(out, fieldnames=['Plate', 'Make'])
                for row in csv.DictReader(inp):
                    if row['Plate'] == plate_num:
                        writer.writerow(row)

            with open('.availablecars.csv', 'r', encoding="utf-8", newline="") as inp, open('.updatecars.csv', 'w', encoding="utf-8", newline="") as out:
                writer = csv.DictWriter(out, fieldnames=['Plate', 'Make'])
                writer.writeheader()
                for row in csv.DictReader(inp):
                    if row['Plate'] != plate_num:
                        writer.writerow(row)
            os.remove(".availablecars.csv")
            os.rename(".updatecars.csv", ".availablecars.csv")
            
            #Fall sem sér um datetime
            start_date = input("Enter start date (D/M/YYYY): ")
            rent_length = int(input("Enter length of rental in days: "))
            dt = datetime.datetime.strptime(start_date, "%d/%m/%Y")
            tdelta = datetime.timedelta(days = rent_length)
            end_date = dt + tdelta
            pop = end_date.strftime("%d/%m/%Y")
            end_end_date = pop
            
            #Reiknað saman flokk bíls með lengd leigu
            fullprice = fullprice * rent_length

            #Tryggingar:
            extra_ins = input("Extra insurance?    yes(y), no(n): ").lower()
            if extra_ins == "y":
                fullfullprice = fullprice + (1000 * rent_length)
                print("The price of the rental is {} with insurance included".format(fullfullprice))
                print("Price without the insurance is: {}".format(fullprice))
            else:
                print("The price for the rental is: {}".format(fullprice))
            new_booking = NewBooking(ssn, car_category, plate_num, start_date, rent_length, end_end_date, extra_ins)
            self.__booking_service.add_booking(new_booking)

            
            #booking_menu_1(action)
        # action == "2":
            #Change booking
            
        # action == "3":
            #Look up booking
            
        # action == "4":
            #Return rental
            
        #
            print("Invalid input! Please try again.\n")