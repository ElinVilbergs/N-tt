from customerservice import CustomerService

print(" ")
print("You can do the following: ")
print("1. Add a customer")
print("2. Look up customer")
print("3. Edit customer")
print("4. Unregister customer")
print("press q to quit")
print("")

action = ""

while(action != "q"): 
    election_menu = CustomerService()

    action = input("Choose an option: ").lower()

    if action == "1":
        CustomerService.ui_menu_1(action)   #útfært

    elif action == "2":
        CustomerService.ui_menu_2(action)   #í vinnslu
    
    elif action == "3":
        CustomerService.ui_menu_3(action)

    elif action == "4":
        CustomerService.ui_menu_4(action)

        