import csv

def read_dictionary(filename, key_column_index):
    student_dictionary = {}

    with open(filename, "rt") as csv_file:
        
        csv_reader = csv.reader(csv_file, delimiter=",")

        next(csv_reader)

        for row in csv_reader:
            key_value = row[key_column_index]
            student_dictionary[key_value] = row

    return student_dictionary

def main():
    KEY_INDEX=0 
    NAME_INDEX=1
    students=read_dictionary("students.csv", KEY_INDEX)
    inumber=input("please enter an I-Number: ")
    inumber=inumber.replace("-", "")

    if not inumber.isdigit():
        print("Invalid I-Number")
    elif len(inumber) !=9:
        print("An I-Number must be 9 digits long")
    else:
        if inumber in students:
            student=students[inumber]
            name=student[NAME_INDEX]
            print(f"The student's name is {name}")
        else:
            print("No such student!")



if __name__ == "__main__":
    main()