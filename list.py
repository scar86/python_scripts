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


beatles = ["john","paul","george","ringo","stuart"]
beatles.remove("stuart")
print beatles


d = {'key1' : 1, 'key2' : 2, 'key3' : 3}

print d["key1"]


d["key4"] = 4

print d["key4"]

print d

my_dict = {
    "fish": ["c", "a", "r", "p"],
    "cash": -4483,
    "luck": "good"
}
print my_dict["fish"][0]




once  = {'a': 1, 'b': 2}
twice = {'a': 2, 'b': 4}
for key in once: # for on a hash/dictionary
    print "Once: %s" % once[key]
    print "Twice: %s" % twice[key]




animal_sounds = {
    "cat": ["meow", "purr"],
    "dog": ["woof", "bark"],
    "fox": [],
}
print animal_sounds["cat"]
print animal_sounds


students = ["lloyd", "alice", "tyler"]

for student in students:
    print student


    
