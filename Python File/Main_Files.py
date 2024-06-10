
from Print import print_inventory , MAX_RENT_ITEMS
from Operation_Files import rent_equipment, return_equipment



print("\n")
print("\n")
print("\t \t \t \t \t \t \t \t \t \tFashion Plaza")
print("\n")
print("\t \t \t \t \t \t \t \t Lahan-1(Siraha)| Phone NO:-9824707814")
print("\n")
print("-----------------------------------------------------------------------------------------------------------------------------------------")
print("\t \t \t \t \t \t \t Welcome to Fashion Plaza - Build Your Style, Connect Your World!")
print("-----------------------------------------------------------------------------------------------------------------------------------------")
print("\n")

 



def main():
    rented_items_dict = {}  # Dictionary to store rented items for each customer
    returns = []
    rentals = []
    
    while True:
        print("Employes Only")
        print("\nMenu:")
        print("1. Rent Equipment")
        print("2. Return Equipment")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")
        
        if choice == '1':
            customer_name = input("Enter Customer Name: ")
            

            print("Available Items:")
            print("--------------------------------------------------------------------------------------")
            print_inventory()
            print("--------------------------------------------------------------------------------------")
            
            
            while True:
            
                 num_items = input("Number of Equipment Items to Rent: ")
                 if not num_items.isdigit():
                       print("Please enter a valid integer.")
                       continue
                 num_items = int(num_items)
                 if num_items > MAX_RENT_ITEMS:
                    print(f"You can rent a maximum of {MAX_RENT_ITEMS} items at a time.")
                    continue
                 break
            
            rentals = []
            for i in range(num_items):
                loop = True
                while loop == True:
                    try:
                        code = int(input(f"Enter Equipment Code {i+1}: "))
                        quantity = int(input(f"Enter Quantity {i+1}: "))
                        loop=False
                        if code <= 0 or quantity <= 0:
                            print("Please enter valid positive integers for code and quantity.")
                            continue
                        rentals.append({'code': code, 'quantity': quantity})
                        break
                    except:
                        print("Please enter valid positive integers for code and quantity.")
                       
                        
             # Store rented items in the dictionary
            if customer_name not in rented_items_dict:
                rented_items_dict[customer_name] = []
            rented_items_dict[customer_name].extend(rentals)
            # Update inventory table with new item quantities after adding them to rental list
            
            result = rent_equipment(customer_name, rentals, rented_items_dict)
            print(result)
            print("--------------------------------------------------------------------------------------")
            print("\nUpdated Inventory Stock:")
            print_inventory()
            print("--------------------------------------------------------------------------------------")
            print()
    
            
        elif choice == '2':
            customer_name = input("Enter Customer Name: ")
            print_inventory()  # Display inventory stock
           
            
            while True:
                
                    num_items = input("Number of Equipment Items to Return: ")
                    if not num_items.isdigit():
                       print("Please enter a valid integer.")
                       continue
                    num_items = int(num_items)
                    break
            
            returns = []
            for i in range(num_items):
                loop = True
                while loop == True:
                    try:
                        code = int(input(f"Enter Equipment Code {i+1}: "))
                        quantity = int(input(f"Enter Quantity {i+1}: "))
                        loop=False
                        if code <= 0 or quantity <= 0:
                            print("Please enter valid positive integers for code and quantity.")
                            continue
                        returns.append({'code': code, 'quantity': quantity})
                        break
                    except ValueError:
                        print("Only valid  integers for code and quantity.")
            # Check if entered customer name matches rented items' records
            if customer_name in rented_items_dict:
                print(f"Items for {customer_name}:")
                for item in rented_items_dict[customer_name]:
                    print(f"Equipment Code: {item['code']}, Quantity: {item['quantity']}")
                result = return_equipment(customer_name, returns, rented_items_dict)
                print(result)
                print("--------------------------------------------------------------------------------------")
                print("\nUpdated Inventory Stock:")
                print_inventory()  # Display updated inventory stock after returns
                print("--------------------------------------------------------------------------------------")
                print()

            else:
                print("Customer name does not match rented records. Please enter a valid customer name.")
            
        elif choice == '3':
              break
        else:
             print("Invalid choice, please select 1, 2, or 3.")

    print("Thanks for using our software!")
if __name__ == "__main__":
    main()
