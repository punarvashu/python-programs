# Exercise 5

import datetime


def getTime():
    return datetime.datetime.now()


def enterLog(l):
    if l == 1:
        c = int(input("Enter 1 for exercise and 2 for Food"))
        if (c == 1):
            value = input("Type Here\n")
            with open("jaan-ex.txt", "a") as f:
                f.write(str([str(getTime())]) + ": " + value + "\n")
                print("Succesfully Written")

        elif (c == 2):
            value = input("Type Here\n")
            with open("jaan-food.txt", "a") as f:
                f.write(str([str(getTime())]) + ": " + value + "\n")
                print("Successfully Written")
    elif l == 2:
        c = int(input("Enter 1 for exercise and 2 for Food"))
        if (c == 1):
            value = input("Type Here\n")
            with open("jigar-ex.txt", "a") as f:
                f.write(str([str(getTime())]) + ": " + value + "\n")
                print("Succesfully Written")
        elif (c == 2):
            value = input("Type Here\n")
            with open("jigar-food.txt", "a") as f:
                f.write(str([str(getTime())]) + ": " + value + "\n")
                print("Successfully Written")
    elif l == 3:
        c = int(input("Enter 1 for exercise and 2 for Food"))
        if (c == 1):
            value = input("Type Here\n")
            with open("tunnu-ex.txt", "a") as f:
                f.write(str([str(getTime())]) + ": " + value + "\n")
                print("Succesfully Written")
        elif (c == 2):
            value = input("Type Here\n")
            with open("tunnu-food.txt", "a") as f:
                f.write(str([str(getTime())]) + ": " + value + "\n")
                print("Successfully Written")

    else:
        print("enter valid input")


def readLog(r):
    if (r == 1):
        c = int(input("Enter 1 for Exercise and 2 for food"))
        if c == 1:
            with open("jaan-ex.txt") as f:
                for i in f:
                    print(i, end=" ")
        elif c == 2:
            with open("jaan-food.txt") as f:
                for i in f:
                    print(i, end=" ")
    elif (r == 2):
        c = int(input("Enter 1 for exercise and 2 for food"))
        if c == 1:
            with open("jigar-ex.txt")as f:
                for i in f:
                    print(i, end=" ")
        elif c == 2:
            with open("jigar-food.txt") as f:
                for i in f:
                    print(i, end=" ")
    elif (r == 3):
        c = int(input("Enter 1 for exercise and 2 for food"))
        if c == 1:
            with open("tunnu-ex.txt")as f:
                for i in f:
                    print(i, end=" ")
        elif c == 2:
            with open("tunnu-food.txt") as f:
                for i in f:
                    print(i, end=" ")
    else:
        print("enter valid input")


print("Welcome to Health Management System")
a = int(input("Enter 1 to log the detail and 2 for read the Log"))
if a == 1:
    b = int(input("Enter 1-for Jaan, 2-for Jigar, and 3-for Tunnu"))
    enterLog(b)
elif a == 2:
    b = int(input("Enter 1-for Jaan, 2-for Jigar, and 3-for Tunnu"))
    readLog(b)
else:
    print("Enter valid input")
