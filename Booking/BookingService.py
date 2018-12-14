from BookingRepository import BookingRepository
from NewBooking import NewBooking
import datetime
present = datetime.datetime.now()

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

    #########################################################

    def booking_menu_1(self):
        print("You've selected menu 1")
        balance = 0
        print("Customer needs to be registerd")
        ssn = input("Enter customer social security number: ")
        car_category = input("Enter car category: 1,2 or 3: ")
        if car_category == "1":
            fullprice = balance + 12000
        elif car_category == "2":
            fullprice = balance + 23000
        elif car_category == "3":
            fullprice = balance + 50000
        else:
            print("Error")

        plate_num = input("Enter car plate numer")
        BookingRepository.add_to_booking(self, plate_num)

        #Fá leigutíma:
        starte_date = input("Enter start date (D/M/YYYY): ")
        dte = datetime.datetime.strptime(starte_date, "%d/%m/%Y")
        if dte < present:
            print("Error date has passed")
            start_date = input("Enter start date (D/M/YYYY): ")
        starte_date = start_date
        dt = datetime.datetime.strptime(start_date, "%d/%m/%Y")
                            
        rent_length = int(input("Enter length of rental in days: "))
        tdelta = datetime.timedelta(days = rent_length)
        end_date = dt + tdelta
        pop = end_date.strftime("%d/%m/%Y")
        end_end_date = pop

        #Reikna út fullt verð:
        fullprice = fullprice * rent_length
        extra_ins = input("Extra insurance?    yes(y), no(n): ").lower()
        if extra_ins == "y":
            fullfullprice = fullprice + (1000 * rent_length)
            print("The price of the rental is {} with insurance included".format(fullfullprice))
            print("Price without the insurance is: {}".format(fullprice))
        else:
            print("The price for the rental is: {}".format(fullprice))

        #Velja greiðsluleið:
        credit_card = input("Please enter the credit card number to confirm the booking: ")
        payment = input("Choose a payment method: 1. for credit card, 2. for debit card, 3. for cash: ")
        payment_method = ""
        if payment == "1":
            payment_method = "Credit card"
            credit = input("Enter credit card number: ")
            while len(credit) != 16:
                print("Error, try again")
                credit = input("Enter credit card number: ")
            card_name = input("Enter cardholder name: ") #prump
            exp_date = input("Enter expiration date (M/Y): ") #prump
            cvv = input("Enter CVV number: ")
            while len(cvv) != 3:
                print("Error, try again")
                cvv = input("Enter CVV number: ")
            print("Payment successful")
        elif payment == "2":
            payment_method = "Debit card"
            debit = input("Enter debit card number: ")
            while len(debit) != 16:
                print("Error, try again")
                debit = input("Enter debit card number: ")
            card_name = input("Enter cardholder name: ")
            exp_date = input("Enter expiration date (M/Y): ") #prump
            cvv = input("Enter CVV number: ")
            while len(cvv) != 3:
                print("Error, try again")
                cvv = input("Enter CVV number: ")
            print("Payment successful")
        elif payment == "3":
            payment_method = "Cash"
            print("Payment successful")
        new_booking = NewBooking(ssn, car_category, plate_num, start_date, credit_card, end_end_date, extra_ins, payment_method)
        #self.__booking_repo.add_booking(new_booking)  #
        BookingRepository.add_booking(self, new_booking)

    def booking_menu_2(self):
        plate_num = input("Enter the plate number: ")
