class Customer:
    def __init__(self, first, last, ssnum, email, phone): #first = Fornafn, last = Eftirnafn, ssnum = kennitala, email = netfang, phone = símanúmer
        self.__first = first
        self.__last = last
        self.__ssnum = ssnum
        self.__email = email
        self.__phone = phone

    def __str__(self):
        return "Full name: {} {}, Social security number: {}, email: {}, Phone: {}".format(self.__first, self.__last, self.__ssnum, self.__email, self.__phone)

    def get_first(self):
        return self.__first
    
    def get_last(self):
        return self.__last
    
    def get_ssnum(self):
        return self.__ssnum

    def get_email(self):
        return self.__email
    
    def get_phone(self):
        return self.__phone
    