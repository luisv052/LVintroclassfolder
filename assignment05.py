# --------------------------------------------------------------------------------------- #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              This script helps the user create a text file with tasks and
#              their priorities, it also gives the user the ability to add, remove, and
#              keep track of the tasks.
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# LVilla,2.16.21,Added code to complete assignment 5
# -------------------------------------------------------------------------------------- #

# -- Data -- #
# declare variables and constants
strFile = "C:\\FoundationsPython\\ClassModules\\module05\\assignments\\ToDoList.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # A Capture the user option selection
strMenu = """
    Menu of Options
    1) Show current data
    2) Add a new item
    3) Remove an existing item
    4) Save changes to file
    5) Exit Program
"""  # A menu of user options


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# structure the data visually
objFile = open(strFile, "r")

for row in objFile:
    lstRow = row.split(",")
    dicRow = {"task": lstRow[0].strip(), "priority": lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print(strMenu)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for row in lstTable:
            print(row["task"], row["priority"], sep=",")
        continue
    # Step 4 - Add a new item to the list/Table
    # restrict priority input for future organization
    # restart the loop if user makes an invalid choice for priority
    # inform the user when a change has been made
    elif (strChoice.strip() == '2'):
        dicTask = input("Enter a Task: ")
        dicPriority = input("Enter it's priority [L]ow [M]edium or [H]igh: ")
        if dicPriority.lower() == "l" or dicPriority.lower() == "m" or dicPriority.lower() == "h":
            dicRow = {"task": dicTask.strip(), "priority": dicPriority.strip()}
            lstTable.append(dicRow)
            print("\n" + dicTask + "," + dicPriority + " added!")
        else:
            print("\nInvalid input, please choose from [L]ow [M]edium or [H]igh")
        continue
    # Step 5 - Remove an item from the list/Table based on its name
    # restart the loop if user makes an invalid choice for task
    # inform the user when a change has been made
    elif (strChoice.strip() == '3'):
        print("Please choose from the following tasks:\n")
        for row in lstTable:
            print(row["task"] + "," + row["priority"])
        count = 0  # counter used to index hierarchy to avoid improper print statements
        dicTaskRemoved = input("What is the name of the task you would like to remove: ")
        for dicRow in lstTable:
            if dicTaskRemoved.lower() == dicRow["task"].lower():
                lstTable.remove(dicRow)
                count += 1  # counter used to index hierarchy to avoid improper print statements
        if count > 0:  # counter used to index hierarchy to avoid improper print statements
            print("\n" + dicTaskRemoved + " has been removed")
        else:
            print("Invalid Task Selection")
        continue

    # Step 6 - Save tasks to the ToDoList.txt file
    # verify choice before saving
    # restart loop if invalid choice

    elif (strChoice.strip() == '4'):
        strSave = input("Are you sure you want to commit changes? Enter 'Y' or 'N': ")
        if strSave.lower() == "y":
            objFile = open(strFile, 'w')
            for dicRow in lstTable:
                objFile.write(dicRow["task"] + ',' + dicRow["priority"] + '\n')
            objFile.close()
            print("\nData Saved!")

        elif strSave.lower() == "n":
            print("\nPlease continue editing!")
        else:
            print('\nYou have not chosen a valid option, please choose "Y" or "N"')
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Goodbye!!")
        break  # and Exit the program

    # restart the loop if invalid menu choice selected
    else:
        print('That is not a valid option, please choose  [1 to 5]')
