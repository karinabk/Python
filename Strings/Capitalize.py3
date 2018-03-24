#You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
#For example, alison heck should be capitalised correctly as Alison Heck. 
# alison heck = Alison Heck
#Given a full name, your task is to capitalize the name appropriately.

def capitalize(string):
    myList=list(string)
    myList[0] = myList[0].upper()
    for i in range(len(myList)):
        if myList[i]==" ":
            myList[i+1]=myList[i+1].upper()
        # string += "".join(myList) + " "
     
    return "".join(myList)
    
    if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)
