# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# <Armand Feuba Baweu  >,<08/26/2023>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
objFile = None #file handle


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
while (True):
    objFile = open(strFile, "r")
    for row in objFile:
        strData = row.split(",")
        disRow ={"Task": strData[0].strip(), "Priority": strData[1].strip()}
        lstTable.append(disRow)
    objFile.close()
    # -- Input/Output -- #
    # Step 2 - Display a menu of choices to the user
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
        # TODO: Add Code Here
        for row in lstTable:
            print(row["Task"]+"(" +row["Priority"]+")")
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        strTask = str(input("what is the task?")).strip()
        strPriority = str(input("What is the priority? [high|low]")).strip()
        disRow={"Task": strTask,"Priority":strPriority }
        lstTable.append(disRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        strRemove = input("Which task would you like to remove?")
        BooleanRemoved = False #check is data was found and removed
        for row in lstTable:
            task = dis(row).values()
            priority = dis(row).values()
            if  task == strRemove:
                lstTable.remove(row)
                BooleanRemoved = True
            else:
                print("I can't find what you are looking for!!!")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        for row in lstTable:
            print(row["Task"]+"(" + row["Priority"]+ ")")
            if "y" == str(input("do you want to save file? (y/n)")).strip().lower():
                objFile = open(strFile, "w")
                for disRow in lstTable:
                    objFile.write(disRow["Task"]+","+ disRow["Priority"]+"\n")
                objFile.close()
            else:
                print(data is not saved)
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
                break  # and Exit the program
