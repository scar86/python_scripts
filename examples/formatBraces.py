'''Illustrate braces in a formatted string.'''

a = 2
b = 3
setStr = 'The set is {{{a}, {b}}}.'.format(**locals())
print(setStr)
