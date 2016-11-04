#!/usr/bin/python

my_dict = {
    "Nombre": "oscar",
    "Age": 29,
    "Apellido": "pacheco",
    }

print my_dict.items()
print my_dict.keys()
print my_dict.values()

for key in my_dict:
    print key, my_dict[key]


#list comphenention

evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50
