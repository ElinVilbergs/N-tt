from NewBooking import NewBooking
import csv
import os
import datetime

class BookingRepository:

    def __init__(self):
        self.__booking = []

    def add_booking(self, booking):
        with open(".booking.csv", "a+", encoding="utf-8", newline="") as booking_file:
            ssn = booking.get_ssn()
            car_category = booking.get_car_category()
            plate_num = booking.get_plate_num()
            start_date = booking.get_start_date()
            credit_card = booking.get_credit_card()
            end_end_date = booking.get_end_end_date()
            extra_ins = booking.get_extra_ins()
            payment_method = booking.get_payment_method()
            
            booking_file.write("{},{},{},{},{},{},{},{}\n".format(ssn, car_category, plate_num, start_date, credit_card, end_end_date, extra_ins, payment_method))


    def get_booking(self):
        with open(".booking.csv", "r", encoding="utf-8", newline="") as findbooking:
            plate_num = input("Enter plate number: ")
            findbookingreader = csv.DictReader(findbooking)
            for line in findbookingreader:
                if line["Plate"] == plate_num:
                    print(line)

    def add_to_booking(self, plate_num):
        with open('availablecars.csv', 'r', encoding="utf-8", newline="") as inp, open('rentedcars.csv', 'a+', encoding="utf-8", newline="") as out:
                writer = csv.DictWriter(out, fieldnames=['Plate', 'Make'])
                for row in csv.DictReader(inp):
                    if row['Plate'] == plate_num:
                        writer.writerow(row)

        with open('availablecars.csv', 'r', encoding="utf-8", newline="") as inp, open('updatecars.csv', 'w', encoding="utf-8", newline="") as out:
            writer = csv.DictWriter(out, fieldnames=['Plate', 'Make'])
            writer.writeheader()
            for row in csv.DictReader(inp):
                if row['Plate'] != plate_num:
                    writer.writerow(row)
        os.remove("availablecars.csv")
        os.rename("updatecars.csv", "availablecars.csv")

    
    def change_booking(self, plate_num):
        with open(".booking.csv", "r", encoding="utf-8", newline="") as inp, open('newbooking.csv', 'w', encoding="utf-8", newline="") as out:
            writer = csv.DictWriter(out, fieldnames=['Customer SSN', 'Car category', 'Plate', "Starting date", "Credit card", "Ending date", "Extra insurance", "Payment method"])
            writer.writeheader()
            for row in csv.DictReader(inp):
                if row['Plate'] != plate_num:
                    writer.writerow(row)

        os.remove(".booking.csv")
        os.rename("newbooking.csv", ".booking.csv")

        with open('.rentedcars.csv', 'r', encoding="utf-8", newline="") as inp, open('availablecars.csv', 'a+', encoding="utf-8", newline="") as out:
            writer = csv.DictWriter(out, fieldnames=['Plate', 'Make'])
            for row in csv.DictReader(inp):
                if row['Plate'] == plate_num:
                    writer.writerow(row)

        with open('.rentedcars.csv', 'r', encoding="utf-8", newline="") as inp, open('updatecars.csv', 'w', encoding="utf-8", newline="") as out:
            writer = csv.DictWriter(out, fieldnames=['Plate', 'Make'])
            writer.writeheader()
            for row in csv.DictReader(inp):
                if row['Plate'] != plate_num:
                    writer.writerow(row)
        os.remove(".rentedcars.csv")
        os.rename("updatecars.csv", ".rentedcars.csv")

    def remove_booking(self, plate_num):
        
        with open('.rentedcars.csv', 'r', encoding="utf-8", newline="") as inp, open('availablecars.csv', 'a+', encoding="utf-8", newline="") as out:
            writer = csv.DictWriter(out, fieldnames=['Plate', 'Make'])
            for row in csv.DictReader(inp):
                if row['Plate'] == plate_num:
                    writer.writerow(row)

        with open('.rentedcars.csv', 'r', encoding="utf-8", newline="") as inp, open('updatecars.csv', 'w', encoding="utf-8", newline="") as out:
            writer = csv.DictWriter(out, fieldnames=['Plate', 'Make'])
            writer.writeheader()
            for row in csv.DictReader(inp):
                if row['Plate'] != plate_num:
                    writer.writerow(row)
        os.remove(".rentedcars.csv")
        os.rename("updatecars.csv", ".rentedcars.csv")

        with open(".booking.csv", "r", encoding="utf-8", newline="") as inp, open('newbooking.csv', 'w', encoding="utf-8", newline="") as out:
            writer = csv.DictWriter(out, fieldnames=['Customer SSN', 'Car category', 'Plate', "Starting date", "Credit card", "Ending date", "Extra insurance", "Payment method"])
            writer.writeheader()
            for row in csv.DictReader(inp):
                if row['Plate'] != plate_num:
                    writer.writerow(row)
        os.remove(".booking.csv")
        os.rename("newbooking.csv", ".booking.csv")
