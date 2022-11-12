#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# AyersA, 2022-Nov-11, Changed functionality to use dictionary vs list.
#                       Altered, entry, print, and save functionality to use dict.
#                       Added new functionality to load from file and delete items.
# AyersA, 2022-Nov-12, Adjusted the save functionality to check for existing
#                       Entries before saving so we don't save duplicates.
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
lstRow = []  # list of data row
dictRow = {} # dictionary row 
strFileName = 'CDInventory.txt'  # data storage file

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    
    if strChoice == 'l':
        # TODO Add the functionality of loading existing data
        with open(strFileName, 'r') as file_object:
           for row in file_object:
               lstRow = row.strip().split(',')
               dictRow = {'id': int(lstRow[0]), 'title':lstRow[1], 'artist':lstRow[2]}
               lstTbl.append(dictRow)
        print('....loading exisiting data\n')
    
    #ADD ENTIRES
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        
        dictRow = {'id': intID, 'title': strTitle, 'artist': strArtist}
        lstTbl.append(dictRow)
        print('...recording entry\n')
    
    #DISPLAY ENTRIES
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(str(row['id']) + ', ' + row['title'] + ', ' + row['artist'])
        print()
    
    #DELETE ENTRIES
    elif strChoice == 'd':
        toDelete = input('Enter the id number of the entry to delete: ')  
        toDelete = int(toDelete) #cast from string to int so it can find the matching dict row.
        
        for row in lstTbl:
            if row['id'] == toDelete:
                print(f"...Deleting entry #{row['id']} - {row['title']}, {row['artist']}\n")
                row.clear()
            else:
                continue                    
        lstTbl = list(filter(None, lstTbl)) #remove empty dictionary  
    
    #SAVE ENTRIES 
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        # declare variables that are only used in this block
        existlstRow = []
        existdictRow = {}
        existlistTbl = []
        # get existing file contents to compare, and avoid saving things that already exist 
        with open(strFileName, 'r') as file_object:
             for row in file_object:
                 existlstRow = row.strip().split(',')
                 existdictRow = {'id': int(existlstRow[0]), 'title':existlstRow[1], 'artist':existlstRow[2]}
                 existlistTbl.append(existdictRow)       
        # create temp list that saves entries that aren't duplicates  
        temp_list = []
        for entry in lstTbl:
            if entry not in existlistTbl:
                temp_list.append(entry)
            else:
                pass
        # save records
        with open(strFileName, 'a') as file_object:
            for row in temp_list:
                strRow = ''
                for value in row.values():
                    strRow += str(value) + ','
                strRow = strRow[:-1] + '\n'
                file_object.write(strRow)
    else:
        print('Please choose either l, a, i, d, s or x!')

