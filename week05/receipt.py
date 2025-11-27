import csv

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
    KEY_INDEX = 0

    products_dict = read_dictionary("products.csv", KEY_INDEX)
    print(products_dict)

    with open("request.csv", "rt") as csv_file_2:

        csv_reader_2 = csv.reader(csv_file_2, delimiter=",")

        next(csv_reader_2)

        for row in csv_reader_2:
            product_number = row[0]
            quantity =  row[1]

            if product_number in products_dict:
                corresponding_item = products_dict[product_number]

                product_name = corresponding_item[1]
                product_price = corresponding_item[2]

            corresponding_item = products_dict[product_number]
            print(f"{product_name}: {quantity} @ {product_price}")


if __name__ == "__main__":
    main()