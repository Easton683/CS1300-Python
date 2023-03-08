'''Word Encryption Algorithm'''

import random
# -------------------
# DOCTYPE Python
# Easton Jackson CS 1300
# Coding Four
# -------------------

# Get input from user
entryWord = input("Please enter your word to be encoded: ")
firstLetter = entryWord[0]

# Remove first letter for ecryption to be done on remaing chars
s1 = entryWord[1:]

# Remove all vowels
if "a" in entryWord:
    s1 = s1.replace("a", "")
if "e" in entryWord:
    s1 = s1.replace("e", "")
if "i" in entryWord:
    s1 = s1.replace("i", "")
if "o" in entryWord:
    s1 = s1.replace("o", "")
if "u" in entryWord:
    s1 = s1.replace("u", "")

# Make these chars a 1
if "b" or "f" or "p" or "v" in s1:
    s1 = s1.replace("b", "1")
    s1 = s1.replace("f", "1")
    s1 = s1.replace("p", "1")
    s1 = s1.replace("v", "1")

# Make these chars a 2
if "c" or "g" or "j" or "k" or "q" or "s" or "x" or "z" in s1:
    s1 = s1.replace("c", "2")
    s1 = s1.replace("g", "2")
    s1 = s1.replace("j", "2")
    s1 = s1.replace("k", "2")
    s1 = s1.replace("q", "2")
    s1 = s1.replace("s", "2")
    s1 = s1.replace("x", "2")
    s1 = s1.replace("z", "2")

# Make these chars a 3
if "d" or "t" in s1:
    s1 = s1.replace("d", "3")
    s1 = s1.replace("t", "3")

# Make this char a 4
if "l" in s1:
    s1 = s1.replace("l", "4")

# Make these chars a 5
if "m" or "n" in s1:
    s1 = s1.replace("m", "5")
    s1 = s1.replace("n", "5")

# Make this char a 6
if "r" in s1:
    s1 = s1.replace("r", "6")

if "11" or "22" or "33" or "44" or "55" or "66" in s1:
    s1 = s1.replace("11", "1")
    s1 = s1.replace("22", "2")
    s1 = s1.replace("33", "3")
    s1 = s1.replace("44", "4")
    s1 = s1.replace("55", "5")
    s1 = s1.replace("66", "6")

# Add first letter for finalization methods
s1 = firstLetter + s1

# Adding or removing elements to get the length to 4
if len(s1) > 4:
    s1 = s1[0:4]
elif len(s1) < 4:
    while len(s1) < 4:
        s1 = s1 + "0"
print("Encoded message is: ", s1)

# Random numbers added on end to increase cryptography entropy (Creative Element)
# Setting desired length for s2
s2 = "aaaaaaaaaaaaaaaa"
s2 = s1

# Adding the rand numbers
while len(s2) < 16:
    rand = str(random.randint(0, 9))
    s2 = s2 + rand

print("Encoded message with rand to fill 128 bit block is:", s2)
