# Added an additional "except" clause for file permission errors.

import csv
from datetime import datetime


def read_dictionary(filename, key_column_index):

    compound_dictionary = {}

    with open(filename, "rt") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        
        next(csv_reader)

        for row in csv_reader:
            key_value = row[key_column_index]
            compound_dictionary[key_value] = row

    return compound_dictionary


def main():

    try:

        KEY_INDEX = 0

        products_dict = read_dictionary("products.csv", KEY_INDEX)

        all_items_quantity = 0
        subtotal = 0
        sales_tax = 0.06

        with open("request.csv", "rt") as csv_file_2:

            csv_reader_2 = csv.reader(csv_file_2, delimiter=",")

            next(csv_reader_2)

            print("Inkom Emporium")
            for row in csv_reader_2:
                product_number = row[0]
                quantity =  row[1]

                if product_number in products_dict:
                    corresponding_item = products_dict[product_number]

                    product_name = corresponding_item[1]
                    product_price = corresponding_item[2]

                corresponding_item = products_dict[product_number]
                all_items_quantity += float(quantity)
                subtotal += (float(product_price)*float(quantity))
                print(f"{product_name}: {float(quantity)} @ {product_price}")
            
            current_datetime = datetime.now()
            formatted_date = current_datetime.strftime("%a %b %d %H:%M:%S %Y")
            print(f"Number of Items: {all_items_quantity:.0f}")
            print(f"Subtotal: {subtotal:.2f}")
            print(f"Sales Tax: {(sales_tax*subtotal):.2f}")
            print(f"Total: {subtotal+(sales_tax*subtotal):.2f}")
            print(f"Thank you for shopping at the Inkom Emporium")
            print(f"{formatted_date}")
        
    except FileNotFoundError as not_found_err:
        # This code will be executed if the user enters
        # the name of a file that doesn't exist.
        print("Error: missing file")
        print(f"{not_found_err}")

    except PermissionError as perm_err:
        # This code will be executed if the user enters the name
        # of a file and doesn't have permission to read that file.
        print()
        print(type(perm_err).__name__, perm_err, sep=": ")
        print(f"You don't have permission to read {filename}.")
        print("Run the program again and enter the name" \
                " of a file that you are allowed to read.")
        
    except KeyError as key_error:
        # This code will be executed if the user enters
        # an invalid integer for the line number.
        print()
        print(type(key_error).__name__, key_error, sep=": ")
        print("Unknown product ID in the request.csv file.")

if __name__ == "__main__":
    main()