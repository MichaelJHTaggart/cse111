def main():
    list = []
    with open("provinces.txt", "rt") as txt_file:   
        for txt in txt_file:
            clean = txt.strip()
            list.append(clean)
        print(list)
    list.pop(0)
    list.pop()
    print(list)
    for i in range(len(list)):
        if list[i] == "AB":
            list[i] = "Alberta"

    count = list.count("Alberta")

    print(f"Alberta shows up {count} times.")



if __name__ == "__main__":
    main()