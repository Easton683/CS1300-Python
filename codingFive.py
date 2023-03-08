'''FreeFall Calculator'''

# -------------------
# DOCTYPE Python
# Easton Jackson CS 1300
# Coding Five
# 3/6/2023
# -------------------

# Defining functions to get input and check for positive values
def getInput():
    x = input()
    return x

def isValid(h,v):
    v=float(v)
    h=float(h)
    if (h>=0 and v>=0):
        return True
    else:
        return False

# Setting initial values so the loop will run atleast once
h=-1
v=-1

# getting input and using the valid function as the escape from the loop
while(isValid(h,v)==False):
    print("Please enter initial height: ")
    h=getInput()
    print("Please enter intial velocity:")
    v=getInput()

# Casting v and h to float to ensure they work with out functions
v=float(v)
h=float(h)

# Calculating the maximum height
maxHeightTime = v/32
maxHeight = h+v*maxHeightTime-16*maxHeightTime*2
print("The max height of the object will be:", maxHeight)

# Setting secondsPassed as our iterator
secondsPassed = 0
secondsPassed=float(secondsPassed)

# looping until the ball hits the ground
while(h>0):
    h = h+v*secondsPassed-16*secondsPassed*2
    v = v-32.15
    secondsPassed+=.1
print('The ball will hit the ground after',secondsPassed,'seconds')
