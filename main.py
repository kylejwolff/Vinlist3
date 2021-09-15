"""A pyspark version of my Vinlist app"""
from os import system, name
import pymongo


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


def read_csv(file_path):
    arr = []
    try:
        file = open(file_path, "r")
        line = file.readline()
        while line:
            words = line.split(",")
            arr2 = []
            for _i in range(0, len(words)-1):
                arr2.append(words[_i])
            arr.append(arr2)
            line = file.readline()
        return arr

    except FileNotFoundError:
        print(f"Invalid path: {file_path}")
    finally:
        file.close()


my_client = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = my_client["mydatabase"]

clear()
run = True
while run:
    print("+++++++++++++++++++++++++++++")
    print("+ Main menu                 +")
    print("+ 1 - read csv              +")
    print("+ 2 - print current table   +")
    print("+ 3 - push table to MongoDB +")
    print("+ x - exit the program      +")
    print("+++++++++++++++++++++++++++++")
    # print("Enter a menu option from the list: ")
    user_entry = input("Enter a menu option from the list: ")
    if user_entry is "1":
        clear()
        print("This will read a csv")
    elif user_entry is "2":
        clear()
        print("This will print the current table")
    elif user_entry is "3":
        clear()
        print("This will push the table to MongoDB")
    elif user_entry is "x":
        run = False