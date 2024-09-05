def main():
    # name = input("Name : ")
    # house = input("House: ")
    # name, house = get_student()
    s = get_student()
    if s[0] == "Jayesh":
        s[1] = "Venkatadri"
    print(f"{s['name']} from {s['house']}")

# def get_name():
#     return input("Name: ")
#
# def get_house():
#     return input("House: ")

def get_student():
    # s= {}
    # s["name"] = input("Name:")
    # s["house"] = input("House")
    # name = input("Name:")
    # house = input("House: ")
    # return [name,house]
    # name =input("name")
    # house = input("name")
    # return {"name": name, "house": house}
    

if __name__ == "__main__":
    main()