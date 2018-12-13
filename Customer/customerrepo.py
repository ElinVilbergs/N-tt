from registration import Registration
import csv
import os

class CustomerRepository:
    
    def __init__(self):
        self.__customer = []

    def add_customer(self, customer):
        # first add to file then to private list
        with open(".customer.csv", "a+") as customer_file:
            name = customer.get_name()
            mail = customer.get_mail()
            ssn = customer.get_ssn()
            phone = customer.get_phone()
            customer_file.write("{},{},{},{}\n".format(name, mail, ssn, phone))

    def get_customer(self):
        if self.__customer == []:
            with open(".customer.csv", "r") as customer_file:
                for line in customer_file.readlines():
                    name, mail, ssn, phone = line.split(",")
                    new_customer = Registration(name, mail, ssn, phone)
                    self.__customer.append(new_customer)    
        
        return self.__customer

    
    def find_customer(self):
        with open(".customer.csv", "r") as findcustomer:
            ssn = input("Enter customer's social security number: ")
            findcustomerreader = csv.DictReader(findcustomer)

            for line in findcustomerreader:
                if line["Social Security number"] == ssn:
                    print(line)
        
    
    def edit_customer(self):
        ssn = input("Enter the Social security number: ")
        with open(".customer.csv", "r") as inp, open('.newcustomer.csv', 'w') as out:

            writer = csv.DictWriter(out, fieldnames=['Name', 'Email', 'Social Security number', "Phone number"])
            writer.writeheader()
            for row in csv.DictReader(inp):
                if row['Social Security number'] != ssn:
                    writer.writerow(row)

        os.remove(".customer.csv")
        os.rename(".newcustomer.csv", ".customer.csv")
