
def write_inventory(inventory):
    with open('item.txt', 'w') as file:
        for item in inventory:
            line = ','.join([str(item[0]), item[1], item[2], '$' + str(item[3]), str(item[4])]) + '\n'
            file.write(line)

def create_invoice(content, invoice_name):
    with open(invoice_name, 'w') as file:
        file.write(content)