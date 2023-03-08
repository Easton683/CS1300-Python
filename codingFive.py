'''FreeFall Calculator'''

# -------------------
# DOCTYPE Python
# Easton Jackson CS 1300
# Coding Five
# 3/6/2023
# -------------------

# Defining functions to get input and check for positive values


def getInput():
    xInput = input()
    return xInput


def isValid(x, y):
    x = float(x)
    y = float(y)
    if (y >= 0 and x >= 0):
        return True
    else:
        return False


# Setting initial values so the loop will run atleast once
initialHeight = -1
initialVelocity = -1

# getting input and using the valid function as the escape from the loop
while (not isValid(initialHeight, initialVelocity)):
    print("Please enter initial height: ")
    initialHeight = getInput()
    print("Please enter intial velocity:")
    initialVelocity = getInput()

# Casting v h and 2 to float to ensure they work with our functions
initialVelocity = float(initialVelocity)
initialHeight = float(initialHeight)
two = float(2)

# Calculating the maximum height
maxHeightTime = initialVelocity/32
maxHeight = (initialHeight)+(initialVelocity*maxHeightTime)-(16*(maxHeightTime*maxHeightTime))
print("The max height of the object will be:", maxHeight)

# Setting secondsPassed as our iterator
secondsPassed = 0.1
secondsPassed = float(secondsPassed)
height=initialHeight
velocity = initialVelocity

# looping until the ball hits the ground
while height > 0:
    height = height+velocity*secondsPassed-16*(secondsPassed*secondsPassed)
    velocity = velocity-3.215
    secondsPassed = secondsPassed+.1
print('The ball will hit the ground after', secondsPassed, 'seconds')
