import datetime
from datetime import timedelta
from Invoice_notes import generate_unique_invoice_id, generate_rent_invoice, generate_return_invoice
from Print import COMPANY_NAME, ADDRESS, PHONE_NUMBER, EMAIL, LATE_FINE_PER_DAY
from Write_Files import write_inventory, create_invoice
from Read_Files import read_inventory
from Print import print_inventory
#--------------------------------------------------CalculateFee Function----------------------------------------------------
def calculate_late_fee(return_date, due_date):
    days_late = (return_date - due_date).days
    if days_late > 0:
        return days_late * LATE_FINE_PER_DAY
    else:
        return 0
#--------------------------------------------------Rent Function------------------------------------------------------------

def rent_equipment(customer_name, rentals, rented_item_details):
    inventory = read_inventory()
    total_amount = 0
    invoice_content = f'{COMPANY_NAME}\nAddress: {ADDRESS}\nPhone: {PHONE_NUMBER}\nEmail: {EMAIL}\nCustomer Name: {customer_name}\nDate of Rental: {datetime.datetime.today().date()}\n'
   
    rented_item_details = []  # List to store rented item details
    
    for rental in rentals:
        item_found = False
        for item in inventory:
            if rental['code'] == item[0]:
                item_found = True
                if rental['quantity'] > item[4]:
                    print(f"Only {item[4]} {item[1]} available. Cannot rent {rental['quantity']} as requested.")
                    continue
                item[4] -= rental['quantity']
                total_amount += item[3] * rental['quantity']
                rented_item_details.append((item[1], item[2], item[3], rental['quantity']))  # Store item details
        if not item_found:
            print(f"Item with code {rental['code']} not found in inventory.")

     
    
    write_inventory(inventory)
    
    if rented_item_details:
        print() # Print some empty lines
        print()
        result = generate_rent_invoice(customer_name, rented_item_details, total_amount)
        print(invoice_content)
        return result
    else:
        return "No items rented. Invoice not created."
    



#--------------------------------------------------Return Function----------------------------------------------------
    
def return_equipment(customer_name, returns, rented_items_dict):
    valid_return = True  # Initialize valid_return here
    inventory = read_inventory()
    loop = True
    while loop == True:
        try:
            return_date_str = input("Enter the Return Date (YYYY-MM-DD): ")
            return_date = datetime.datetime.strptime(return_date_str, '%Y-%m-%d').date()
           
            break
        except ValueError:
            print("Please enter a valid date in the format YYYY-MM-DD.")

    print_inventory()  # Display inventory stock after customer name is entered
    invoice_content = f'{COMPANY_NAME}\nAddress: {ADDRESS}\nPhone: {PHONE_NUMBER}\nEmail: {EMAIL}\nCustomer Name: {customer_name}\nDate of Return: {return_date}\n'
   
    total_amount = 0
   
    rented_items = rented_items_dict.get(customer_name, [])  # Retrieve rented items for the customer
    returned_item_details = []  # List to store returned item details

    for returned_item in returns:
        item_found = False
        for item in inventory:
            if returned_item['code'] == item[0]:
                item_found = True

                if returned_item['quantity'] > 0:

                    if returned_item['quantity'] > item[4]:
                        print(f"Error: Cannot return more {item[1]} than were rented.")
                        valid_return = False
                    else:
                        returned_item_details.append((item[1], item[2], item[3], returned_item['quantity']))  # Store item details
                        item[4] += returned_item['quantity']
                        total_amount += item[3] * returned_item['quantity']
        if not item_found:
            print(f"Item with code {returned_item['code']} not found in inventory.")
    if not valid_return:
        print("Invalid return. Please make sure you are returning items you have rented.")
        return


    
    write_inventory(inventory)
    
    if returned_item_details:
        due_date = (return_date + timedelta(days=5))
        late_fee = calculate_late_fee(return_date, due_date)

        # Create the invoice content
        invoice_content = generate_return_invoice(customer_name, return_date, returned_item_details, due_date, late_fee, total_amount)
        
        print()
        print()
        print(invoice_content)
        
        unique_invoice_name = generate_unique_invoice_id(customer_name) + "_return_invoice.txt"
        create_invoice(invoice_content, unique_invoice_name)  # Assuming create_invoice saves the content to a file

        return f"Return Invoice created: {unique_invoice_name}"
    else:
        return "No items returned. Invoice not created."






