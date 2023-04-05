'''File Reader'''

# -------------------
# DOCTYPE Python
# Easton Jackson CS 1300
# Coding Eight
# 4/4/2023
# -------------------

'''Separate State and Capital'''
def parseStateCap(originalTxtFile):
    iterator = 0

    # Splitting txt file
    splitlines = originalTxtFile.splitlines()
    while (iterator <= 49):
        # setting tempLine to current line
        tempLine = splitlines[iterator]
        # finding comma index
        commaIndex = tempLine.find(',')
        tempState = tempLine[:commaIndex]
        commaIndex = tempLine.rindex(',')
        tempCapital = tempLine[commaIndex+1:len(tempLine):]

        # testing for uniformity on first letter
        if tempState[0] == tempCapital[0]:
            print(tempState,tempCapital)
        iterator += 1

'''State Lookup Function'''
def stateLookup(state, originalTxtFile):
    # Splitting txt file
    splitlines = originalTxtFile.splitlines()
    iterator = 0
    while (iterator <= 49):
        # finding index for certain substring
        if state in splitlines[iterator]:
            print(splitlines[iterator])
        iterator += 1

# Opening txt file
f = open("StatesANC.txt", "r")
txtFile = (f.read())

# sending file to function
parseStateCap(txtFile)

# asking for input
userState = input("What state would you like to know about?  ")
stateLookup(userState, txtFile)

# Asking user if they want info on every state (Creative Element)
print("Do you want to know about every state? Y or N")
questionAnswer = input()
if questionAnswer =="y" or "Y":
    print(txtFile)