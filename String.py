msg ="Hello world"
print(msg)
print(msg.capitalize())

another_string = 'String with single quotes'
print(another_string)

a_multiline_string ='''This is the string with----- more
than one line'''
print(a_multiline_string)

# If you need to use single quotes in your string then wrap it in double quotes as shown below
an_inside_singlequote_string = "I'm a python programmer"
print(an_inside_singlequote_string)
# If you need to use double quotes in your string then wrap it in single quotes as shown below
an_inside_doublequote_string = 'The word "Python" generally refers to a snake'
print(an_inside_doublequote_string)
tripleString = """Here's another way to embed "quotes" in a string"""
print(tripleString)

# creating string using str method which converts other data types into string..
my_number = 123
my_number_string = str(my_number)
print(my_number_string)

# It is not possible to convert a literal into an interger as shown below.
# x = int("ABC")
# Below exception will occur
# Traceback (most recent call last):
#   File "c:/python/String.py", line 27, in <module>
#     x = int("ABC")
# ValueError: invalid literal for int() with base 10: 'ABC'
# However if it is a number sring then it is possible
x = int(my_number_string)

# Note: String in Python is an immutable type.That means we can't change the value of a string variable once it is created.
my_string = "abc"
# my_string[0]= "d"

# String Concatination
String_One = 'Diebold'
String_Two = "Nixdorf"
String_Three = String_One +' '+ String_Two
print(String_Three)

# String Methods
my_string = 'This is a string !'
my_string_UpperCase = my_string.upper()
print(my_string_UpperCase)
my_string_LowerCase = my_string.lower()
print(my_string_LowerCase)


# To get a list of all string methods use below in te interpreter
dir(my_string)
help(my_string.capitalize)

# We can check the data type of a variable as shown below
print(type(my_string))


# String Slicing:-
my_string = "I like Python!"
print(my_string[0:1]) # This returns the first letter f the string my_string.
print(my_string[:1])  # Output is first letter i.e. I
print(my_string[0:12]) # Output is 1st to 12 digits in my_string
print(my_string[:12]) # Output is 1st to 12 digits in my_string
print(my_string[1:12]) # Output is 2nd to 12 digits in my_string
print(my_string[0:13]) # Output is 1st to 13 digits in my_string
print(my_string[0:-5]) # It will give output from 1st to 14-5=9 digits in my_string
print(my_string[:]) # It will give output of entire string
print(my_string[2:]) # It will give output from 3rd to remaining all digits in the string

'''
We can use string slicing for parsing fixed width
records in files or occasionally for parsing complicated file names that follow a very specific naming
convention. I have also used it in parsing out values from binary-type files. Any job where you need
to do text file processing will be made easier if you understand slicing and how to use it effectively
'''



