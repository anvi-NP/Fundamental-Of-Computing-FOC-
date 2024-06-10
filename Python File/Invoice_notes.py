import datetime
from datetime import timedelta
from Print import COMPANY_NAME, ADDRESS, PHONE_NUMBER, EMAIL
from Write_Files import create_invoice

#--------------------------------------------------generate_unique_invoice Function----------------------------------------------------
def generate_unique_invoice_id(customer_name):
    timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
    return f'{customer_name}_{timestamp}'
#--------------------------------------------------generate_rent_invoice Function----------------------------------------------------
def generate_rent_invoice(customer_name, rented_item_details, total_amount):
    # Formatting the invoice header with company and customer details
    invoice_content = f'{COMPANY_NAME}\nAddress: {ADDRESS}\nPhone: {PHONE_NUMBER}\nEmail: {EMAIL}\nCustomer Name: {customer_name}\nDate of Rental: {datetime.datetime.today().date()}\n'
   # Adding details of rented items to the invoice
    invoice_content += "Items Rented:\n"
    for item in rented_item_details:
        invoice_content += f"- {item[0]} - {item[1]} - ${item[2]} - Quantity: {item[3]}\n"

    invoice_content += f'Total Amount: ${total_amount}\nRented Date: {datetime.datetime.today().date() + timedelta(days=5)}\nNote: Please return the equipment within 5 days to avoid fines.\n'
    # Generate a unique invoice name and create the invoice
    unique_invoice_name = generate_unique_invoice_id(customer_name) + "_rent_invoice.txt"
    create_invoice(invoice_content, unique_invoice_name)
    
    return f"Invoice created: {unique_invoice_name}"
#--------------------------------------------------generate_return_invoice Function----------------------------------------------------
# Function to generate an invoice for returning rented items
def generate_return_invoice(customer_name, return_date, returned_item_details, due_date, late_fee, total_amount):
     # Formatting the invoice header with company and customer details
    invoice_content = f'{COMPANY_NAME}\nAddress: {ADDRESS}\nPhone: {PHONE_NUMBER}\nEmail: {EMAIL}\nCustomer Name: {customer_name}\nDate of Return: {return_date}\n'
  # Adding details of returned items to the invoice
    invoice_content += "Items Returned:\n"
    for item in returned_item_details:
        invoice_content += f"- {item[0]} - {item[1]} - ${item[2]} - Quantity: {item[3]}\n"
        # Adding due date to the invoice
    invoice_content += f'Due Date: {due_date}\n'
    if late_fee > 0:
        invoice_content += f'Late Fee: ${late_fee}\n'
          # Adding total amount to the invoice
    invoice_content += f'Total Amount: ${total_amount + late_fee}\nThank you for returning the equipment.\n'
    
    return invoice_content
