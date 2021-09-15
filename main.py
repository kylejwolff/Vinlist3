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
            words = line.rstrip().split(",")
            arr2 = []
            for _i in range(0, len(words)):
                arr2.append(words[_i])
            arr.append(arr2)
            line = file.readline()
        return arr

    except FileNotFoundError:
        print(f"Invalid path: {file_path}")
    finally:
        file.close()


def print_table(arr: list, arr_title):
    print(f"Title: {arr_title}")
    line = ""
    for _i in range(0, len(arr[0])):
        if len(arr[0][_i]) < 6:
            line = line + "| " + arr[0][_i] + "\t\t"
        else:
            line = line + "| " + arr[0][_i] + "\t"
    print(line)
    line = ""
    for _i in range(0, len(arr[0])):
        line = line + "________________"
    print(line)
    for _i in range(1, len(arr)):
        line = ""
        for _j in range(0, len(arr[0])):
            if len(arr[_i][_j]) < 6:
                line = line + "| " + arr[_i][_j] + "\t\t"
            else:
                line = line + "| " + arr[_i][_j] + "\t"
        print(line)


my_client = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = my_client["mydatabase"]

table = []
title = ""
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
        path = input("Enter the path of the file: ")
        title = path
        table = read_csv(path)
    elif user_entry is "2":
        clear()
        # for line in table:
        #     print(line)
        print_table(table, title)
    elif user_entry is "3":
        clear()
        print("This will push the table to MongoDB")
    elif user_entry is "x":
        run = False
