'''Rose Bowl Winners'''

# -------------------
# DOCTYPE Python
# Easton Jackson CS 1300
# Coding Nine
# 4/11/2023
# -------------------


def main():
    '''main method'''
    # Try keyword with exception handling if file isnt present in the directory
    try:
        with open('Rosebowl.txt', encoding='UTF-8') as f_read:
            rose_bowl_winners = f_read.readlines()
    except FileNotFoundError:
        print("There was an error. Make sure that file exists in the correct directory.")
    # Calling the n_removal method
    winners_enhanced = n_removal(rose_bowl_winners)

    # Calling the winners_fetch method
    dict1 = winners_fetch(winners_enhanced)

    # Sorting the dictionary
    sorted_dict = {k: v for k, v in sorted(
        dict1.items(), key=lambda item: item[1])}
    for k, v in sorted_dict.items():
        if v >= 4:
            print(k, v)
    # Creative element
    print("Here is every winner, sorted from least to most")
    print(sorted_dict)


def winners_fetch(winners):
    '''Fetch each winner'''
    # setting initial valies for iterator dict and a temp
    iterator = 0
    dict1 = {}
    temp = 1

    # Looping through every occurence and making an entry in the dictionary if it doesnt exist
    while iterator < len(winners):
        if winners[iterator] not in dict1:
            dict1[winners[iterator]] = 1
        else:
            temp = dict1[winners[iterator]]
            temp += 1
            dict1[winners[iterator]] = temp

        iterator += 1
    return dict1


def n_removal(lines):
    '''n removal'''

    # Setting initial iterator and # Checking for \n in the list so it can be removed
    iterator = 0
    while iterator < len(lines):
        if '\n' in lines[iterator]:
            lines[iterator] = lines[iterator][0:(lines[iterator].index('\n'))]
        iterator += 1
    return lines


# Calling main method
main()

#This assignment really helped me learn how
# to utilize dictionaries and locate certain indexes in them.
# I really like this tool and hope to utilize them more in the future.
