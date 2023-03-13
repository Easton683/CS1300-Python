'''Alphabet Checker'''

# -------------------
# DOCTYPE Python
# Easton Jackson CS 1300
# Coding Six
# 3/13/2023
# -------------------

# Function to find consecutive letters in string


def isTripleConsecutive(originalString):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    index = 0
    containsAlphabet = False

    # creating a possible solutions variable for creative element
    possibleSolutions = " ", " ", " "
    possibleSolutions = "abc "
    # looping through every possible consecutive lettering format and checking for it in the original string
    while index < 24:
        threeLetterString = alphabet[index:index+3:]
        index += 1
        possibleSolutions += alphabet[index:index+3:]+" "
        if threeLetterString in originalString:
            containsAlphabet = True

    # returning a tuple for the possibleSolutions and containsAlphabet boolean
    return (containsAlphabet, possibleSolutions)


# getting input from the user
inputString = input("Please enter your string you would like to check: ")

# sending the input string to the function
containsAlphabet, possibleSolution = isTripleConsecutive(inputString)

# checking to see if the function returns true or not
if containsAlphabet:
    print("The string does have consecutive letters from the alphabet.")
else:
    print("The string does not have consecutive letters from the alphabet.")
    # printing possible solutions to show the user what solutions in the word can look like
    print("A possible solution would be one of these substrings: ", possibleSolution)
