#!/usr/bin/python

# print Something, on python 3 is print("text")
print "Hello World"


#declare a variable
my_variable = 10

print my_variable

#change variable value
my_variable = 15

print my_variable


#creat a function, spaces are important ! 
def spam():
    eggs = 12
    return eggs
        
print spam()

# multiple lines of comment can be like this
""" esto es una
prueba de comentario 
lol """


# Set count_to equal to the sum of two big numbers
count_to = 8 + 9

print count_to


#Set eggs equal to 100 using exponentiation on line 3!
#exponents 10x10
eggs = 10 ** 2

print eggs


#residuo

#Set spam equal to 1 using modulo on line 3!

spam = 5 % 4

print spam



#stringsd

brian = "Hello life!"


# Assign your variables below, each on its own line!

caesar = "Graham"
praline = "John"
viking = "Teresa"



# Put your variables above this line

print caesar
print praline
print viking


"""
The string "PYTHON" has six characters,
numbered 0 to 5, as shown below:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

So if you wanted "Y", you could just type
"PYTHON"[1] (always start counting from 0!)
"""
fifth_letter = "MONTY"[4] 

print fifth_letter

# print lenght of the string
parrot = "Norwegian Blue"
print len(parrot)

#all lower

parrot = "Norwegian Blue"

print parrot.lower()


#all upper

parrot = "norwegian blue"

print parrot.upper() 


# transform number 3.14 to string "3.14"
pi = 3.14
print str(pi)

#mehod that have a . (dot) only work on strings
ministry = "The Ministry of Silly Walks"

print len(ministry) 
print ministry.upper()

# Print the concatenation of "Spam and eggs" on line 3!


print "Spam " + "and " + "eggs"

print "The value of pi is around " + str(3.14)


#replace a string on print

string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

#input and printing

name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)
