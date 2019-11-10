# Section 02-1
# Python Basic Coding
# Print

# Basic Print
print('Hello Python!')
print("Hello Python!")
print("""Hello Python!""")
print('''Hello Python!''')

print()

# Using Seperator Option
print('T', 'E', 'S', 'T', sep='')
print('2019', '02', '19', sep='-')
print('niceman', 'google.com', sep='@')

# Using End Option
print('Welcome To', end=' ')
print('the black paradise', end=' ')
print('piano notes')
print('testtest')

print()

# Using format [], {}, ()
print('{} and {}'.format('You', 'Me'))

print("{0} and {1} and {0}".format('You', 'Me'))

print("{a} are {b}".format(a='You', b='Me'))
print("%s's favorite number is %d" % ('Python', 3)) #%s : 문자, %d: 정수, %f : 실수

print("Test1: %5d, Price: %4.2f" % (776, 6534.123))
print("Test1: {0: 5d}, Price:{1: 4.2f}".format(776, 6534.123))
print("Test1: {a: 5d}, Price:{b: 4.2f}".format(a=776, b=6534.123))

# escape code

print("'you'")
print('\'you\'')
print('"you"')
print("""'you'""")
print('\\you\\\n')
print('\t\t\ttest')
