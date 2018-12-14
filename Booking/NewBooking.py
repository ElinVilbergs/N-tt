class NewBooking:
    def __init__(self, ssn, car_category, plate_num, start_date, credit_card, end_end_date, extra_ins, payment_method):
        self.__ssn = ssn
        self.__car_category = car_category
        self.__plate_num = plate_num
        self.__start_date = start_date
        self.__credit_card = credit_card
        self.__end_end_date = end_end_date
        self.__extra_ins = extra_ins
        self.__payment_method = payment_method

# ssn = kennitala, card_info = kortaupplýsingar, car_category = flokkur bíls,
# extend_rent = lengd leigu, extra_ins = auka trygging

    def __str__(self):
        return "{},{},{},{},{},{},{},{}".format(self.__ssn, self.__car_category, self.__plate_num, self.__start_date, self.__credit_card, self.__end_end_date, self.__extra_ins, self.__payment_method)

    def get_ssn(self):
        return self.__ssn

    def get_car_category(self):
        return self.__car_category

    def get_plate_num(self):
        return self.__plate_num

    def get_start_date(self):
        return self.__start_date

    def get_credit_card(self):
        return self.__credit_card

    def get_end_end_date(self):
        return self.__end_end_date

    def get_extra_ins(self):
        return self.__extra_ins

    def get_payment_method(self):
        return self.__payment_method

'''
    def select_category(self):
        car_category = input("Enter car category; 1, 2 or 3")
        balance = 0

        if car_category == "1":
            fullprice = balance + 12000
        elif car_category == "2":
            fullprice = balance + 23000
        elif car_category == "3":
            fullprice = balance + 50000
        else:
            print("Invalid input, please try again")
            #Setja svo loopu þannig ef það er valið vitlaust að hann reyni aftur
        return fullprice
'''
        