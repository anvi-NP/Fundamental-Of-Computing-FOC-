from Read_Files import read_inventory

# Constants
COMPANY_NAME = "Fashion Plaza"
ADDRESS = "LAHAN-1"
PHONE_NUMBER = "9824707814"
EMAIL = "npai4s230020@gmail.com"
MAX_RENT_ITEMS = 20
LATE_FINE_PER_DAY = 10

def print_inventory():
    inventory = read_inventory()
    print("\nInventory Stock:")
    print("SN\tName\t\t\t\tDescription\t\tPrice\tQuantity")
    for item in inventory:
        print(f"{item[0]}\t{item[1]}\t{item[2]}\t{item[3]}\t{item[4]}")