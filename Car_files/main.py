from UI.SalesmanUiþ import SalesmanUi
from UI.SalesmanUI import SalesmanUI
from UI.SalesmanUIB import SalesmanUIB

print("Pick 1 for Cars")
print("Pick 2 for Customers")
print("Pick 3 for Booking")

choice = int(input("Enter number: "))
if choice == 1:
    SMUI = SalesmanUI
elif choice == 2:
    SMUI = SalesmanUi
elif choice == 3:
    SMUI = SalesmanUIB



def main():
    ui = SMUI()
    ui.main_menu()

main()


