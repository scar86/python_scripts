#!/usr/bin/python

print "Pig Latin"

pig = 'ay'

print "Welcome to the Pig Latin translator"

original = raw_input("Enter a Word : ")

if len(original) > 0 and original.isalpha() :
    print original
    word = original.lower()
    first = original[0]
    new_word = word + first + pig
    print new_word
    new_word = new_word[1:len(new_word)]
    print new_word
else:
    print "You don't type anything"
