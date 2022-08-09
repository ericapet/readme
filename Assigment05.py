# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Erica Peterson,08/08/2022,Added code to complete assignment 5
# Erica Peterson,08/09/2022,Completed Script
# ------------------------------------------------------------------------ #
# -- Data -- #
# declare variables and constants
objFile = 'ToDoList.txt'  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
lstRow = []
# -- Processing -- #
# Step 1 - When the program starts, load the data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open("ToDoList.txt",'a')
objFile = open("ToDoList.txt",'r')
print("Here is what is on your To Do List currently: ")
for row in objFile:
    print(lstRow)
    lstRow = row.split(",")
    dicRow= {"Task": lstRow[0].strip(), "Priority": lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()
# Step 2 - Display
# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print('Your current Data is')
        for item in lstTable:
            print(item['Task'] + ',' + item['Priority'])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = (input("Enter a Task: "))
        strPriority = (input("Enter a Priority: "))
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strRemove = input("Task to Remove: ")
        for row in lstTable:
            if row['Task'].lower() == strRemove.lower():
                lstTable.remove(row)
                print("Task Has Been Removed")
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open('ToDoList.txt', 'w')
        for row in lstTable:
            objFile.write(row['Task'] + ' , ' + row['Priority'] + '\n')
        objFile.close()
        print("Data Saved!")
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        print("Would you like to exit program?")
        exit = input("Enter 'y' or 'n': ")
        if (exit == "y"):
            break  # and Exit the program
