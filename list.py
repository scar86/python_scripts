#!/usr/bin/python

zoo = ["dog", "cat", "fish", "monkey"]

if len(zoo) > 3:
    print "first " + zoo[0]
    print "Second " + zoo[1]
    print "Third " + zoo[2]
    print "Fourth " + zoo[3]


zoo[0] = "meh"

print zoo[0]

zoo.append("whaat")

print len(zoo)
 #slice a list

print zoo[0:2]



letters = ['a', 'b', 'c', 'd', 'e']
slice = letters[1:3]
print slice
print letters

#slice a string
animals = "catdogfrog"
print animals[:3]
print animals[3:6]
print animals[6:]

#SEARCH FOR AN INDEX
animals = ["ant", "bat", "cat"]
print animals.index("bat")

# insert at a specific index
animals.insert(1, "dog")
print animals
