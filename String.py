msg ="Hello world"
print(msg)
print(msg.capitalize())

another_string = 'String with single quotes'
print(another_string)

a_multiline_string ='''This is the string with more
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





