'''Random Number Guesser'''

# -------------------
# DOCTYPE Python
# Easton Jackson CS 1300
# Final Exam
# 4/11/2023
# -------------------

import random


def get_difficulty():
    '''Method to get difficulty'''
    # Setting loop to true so it will run until something is returned
    while True:
        # Asking for user input
        user_input = input(
            "What difficulty would you like? H = Hard, N = Normal, E = Easy  ")
        # Checking user input and running through loop again if none of these conditions are met
        if user_input == 'E':
            return 25
        elif user_input == 'N':
            return 50
        elif user_input == 'H':
            return 100
        else:
            print("There was an error, please try again")


def guess(answer, difficulty):
    '''Method to handle guesses'''
    # Setting counter to 1 so we can count the amount of
    # guesses it takes and notifying the user to guess
    counter = 1
    print("I picked a random number in between 0 and",
          difficulty, ". You may start guessing.")

    while True:

        # Setting initial value to false so if it is an int
        # we can change it to true to get out of the loop.
        is_int = False
        while not is_int:
            temp_guess = input("What is your guess? ")

            # Casting guess to int, if it does not work we start the loop again.
            try:
                temp_guess_int = int(temp_guess)
                is_int = True
            except ValueError:
                print("You did not enter a number. Please try again.")

        # Checking to see if it is the right answer and if it is we will break the loop.
        if temp_guess_int == answer:
            print("You solved it! It took you", counter, "guesses.")
            break
        elif temp_guess_int > answer:
            print("Too High!")
            counter += 1
        else:
            print("Too Low!")
            counter += 1


def main():
    '''main method to do basic functions'''
    # Asking user they difficulty they would like to have (Creative Element)
    difficulty = get_difficulty()

    # Generating Random Number with set difficulty
    rand = int(random.randint(1, difficulty))

    # Calling guessing method to start guessing process
    guess(rand, difficulty)


# Calling main method to kick start the program
main()

# I learned many things about coding through this course.
# I have come to believe that python is by far my favorite language
# I also have come to appreciate some things about Java
# Overall, I have obtained a more nuanced and knowledgable opinion on both of them
# The course was great as I was able to learn things on my own
# When programming I much prefer learning on my own and this course
# allowed for that in the best way.