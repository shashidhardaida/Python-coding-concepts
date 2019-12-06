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


# We can use string slicing for parsing fixed width
# records in files or occasionally for parsing complicated file names that follow a very specific naming
# convention. I have also used it in parsing out values from binary-type files. Any job where you need
# to do text file processing will be made easier if you understand slicing and how to use it effectively


                                                                      # ------:STRING FORMATTING:-------#

# String formatting (AKA substitution) is the topic of substituting values into a base string

# 1.Old Way of Substituting Strings 
# In this method we put %s symbol in the string. This means that there is a new string going to come in place of %s.
my_string = "I like %s" % "Python" # Here the part "Python" is going to add in the string my_string
print(my_string)
var = 'cookies'
my_string ="I like %s" % var
print(my_string) # output will be 'I like cookies'
new_string = "I like %s and %s" %("Python", var)
print(new_string) # output is 'I like Python and cookies'
# The rule is we need to pass as many strings as %s symbols are used. Otherwise we will get below error.
#new_string = "I like %s and %s" % "Python"
#  File "d:/Python/Python/String.py", line 94, in <module>
#     new_string = "I like %s and %s" % "Python"
# TypeError: not enough arguments for format string
# --Inserting integeres and floats into a string -- #
my_string = "%i + %i = %i" %(1,2,3)
print(my_string)
float_string = "%f" %(1.23)
print(float_string)
float_string = '%.2f' %(1.23)
print(float_string) # output will be rounded to two decimal places i.e. 1.23
float_string = '%.3f' %(1.23578)
print(float_string) # output will be rounded to two decimal places i.e. 1.236

# 2. New method of string formatting
# In this method we use key value pair as shown below
print("%(lang)s is fun!" % {"lang":"Python"})
# Here basically we just changed our %s into %(lang)s, which is
# basically the %s with a variable inside it. The second part is actually called a Python dictionary that
# we will be studying in the next section. Basically it’s a key:value pair, so when Python sees the key
# “lang” in the string AND in the key of the dictionary that is passed in, it replaces that key with its
# value
# More Examples
print("%(value)s %(value)s %(value)s" % {"value":"SPAM"}) # output is SPAM SPAM SPAM
# After version 2.4 string formatting is done directly by using one module i.e. format() as shown below
my_string = "Python is as simple as {0}, {1}, {2}".format("a","b","c")
print(my_string)
xy= {"x":0, "y":10}
print("Graph a point at where x={x} and y={y}".format(**xy))




