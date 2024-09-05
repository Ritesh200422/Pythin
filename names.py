# names = []
#
# for _ in range(3):
#     names.append(input("What is your name ? "))
#
# for name in sorted(names):
#      print(f"hello , {name}")
#
# name = input("What is your name ")
#
# # file = open("names.txt","a")
# # file.write(f"{name}\n")
# # file.close()
# with open("names.txt","a") as file:
#     file.write(f"{name}\n")

# with open("names.txt","r") as file:
#     lines=file.readline()
#
# for line in lines :
#     print("hello,",line.rstrip())
#

# names=[]
# with open("names.txt") as file:
#     for line in file:
#         names.append(line.strip())
#
# for name in sorted(names):
#     print(f"hello, {name}")
# with open("names.txt") as file:
#     for line in sorted(file,reverse=True):
#         print("hello,",line.rstrip())


# with open("students.csv") as file:
#     for line in file:
#         name,house = line.rstrip().split(",")
#         print(f"{name} is in {house}")
# import csv
#
# students = []
#
# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "house": row["house"]})
# for student in sorted(students, key =lambda student: student["name"]):
#     print(f"{student['name']} is in {student['house']}")

 # for line in file:
    #     name,house = line.rstrip().split(",")
    #     student = {"name": name, "house": house}
    #     students.append(student)
# def get_house(student):
#     return student["house"]

import csv

name=input("Whats Your name")
home=input("Where Do You live")

with open("nagesh.csv","a") as file:
    writer = csv.DictWriter(file,fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})