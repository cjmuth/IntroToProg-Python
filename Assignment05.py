# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# CMuth, 11/12/22,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
strFile = "ToDoList.txt"  # Name of the file to use
objFile = None  # An object that represents a file


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

#Read from the data file
#Open the file in read mode
objFile = open(strFile, "r")
#Loop through rows in data file
for row in objFile:
    #Read data row from file as list
    lstRow = row.split(",")
    #Save list data to dictionary
    dicRow = {'Task': lstRow[0], "Priority": lstRow[1].strip()}
    #Add dictionary to table list
    lstTable.append(dicRow)
#When end of rows, Close file
objFile.close()


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
        if lstTable:
            # Loop through dictionaries in list
            for row in lstTable:
                #   Print values to screen
                print('{}\t\t{}'.format(row['Task'], row['Priority']))
        else:
            print('There are no items in the TODO list.')
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # Get user input as dictionary
        dicRow = {'Task': input('What you you want to do? '), 'Priority': input('What is the priority? ')}
        # Add new dictionary to lstTable
        lstTable.append(dicRow)
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        if lstTable:
            # Get TODO item to be removed
            strRemove = input('\nEnter the TODO item to be removed. ')
            # Remove the indicated dictionary from list
            for row in lstTable:
                if row['Task'] == strRemove:
                    lstTable.remove(row)
        else:
            input('There are no items to remove.\nPress Enter to return to menu.')
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        # Open the file in write mode
        objFile = open(strFile, 'w')
        # Loop through dictionaries in table list
        for row in lstTable:
            # Extract values, concantenate as string, write to text file
            objFile.write(row['Task'] + ',' + row['Priority'] + '\n')
        # Close text file
        objFile.close()
        print('---Changes have been saved---\n')
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        break  # and Exit the program