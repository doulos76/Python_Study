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

