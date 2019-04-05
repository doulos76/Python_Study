# -*- coding: utf-8 -*-
# section02-1
# Python Basic Coding
# Understand of Print Syntax
# Reference : https://www.python-course.eu/python3_formatted_output.php

# Basic Print
print('Hello Python!')
print("Hello Python!")
print("""Hello Python!""")
print('''Hello Python!''')

print()

# Usage of Separator Option

print('T', 'E', 'S', 'T', sep='')
print('T', 'E', 'S', 'T', sep='-')
print('niceman', 'google.com', sep='@')
print('one', 'two', 'three', sep='')

# Usage of End Option
print('Welcom To', end=' ')
print('the black parade', end=' ')
print('piano notes')

# Usage of Format [], {}, ()
print('{} and {}'.format('You', 'Me'))
print("{0} and {1} and {0}".format('You', 'Me'))
print("{a} are {b}".format(a='You', b='Me'))

#%s : String, %d : Integer, %f : Float Number
print("%s's favorite number is %d" % ('EunJee', 7)) 

print("Test1: %5d, Price: %4.2f" %(776, 6534.123))
print("Test1: {0: 5d}, Price: {1: 4.2f}".format(776, 6534.123))
print("Test1: {a: 5d}, Price: {b: 4.2f}".format(a=776, b=6534.123))

# escape code
"""
\n : 개행

"""

print("'you'")
print('\'you\'')
print('"you"')
print("""'you'""")
print('\\you\\\n')
print('test')

print('\t\t\ttest')
