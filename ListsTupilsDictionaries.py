                                                                  # --: LISTS :- #

# A Python list is similar to an array in other languages. In Python, an empty list can be created in the following ways.
my_list = []
my_list = list()
my_list1 = [1,2,3]
print(my_list1)
my_list2 = ["a",'b',"c"]
print(my_list2)
my_list3 = ["a",2 ,"Python",4]
print(my_list3)

# We can also create list of lists as shown below
my_nested_list = [my_list1, my_list2, my_list3]
print(my_nested_list)

# Occasionally, you’ll want to combine two lists together. The first way is to use the extend method:
combo_list = []
one_list = [4,5]
combo_list.extend(one_list) # This extends the combo_list by adding one_list
print(combo_list)

# A slightly easier way is to just add two lists together
my_list1 = [1,2,3]
my_list2 = ['a','b','c']
combo_list = my_list1 + my_list2
print(combo_list)

# Sorting lists
alpha_list = [34,68,8,9,13,0]
print(alpha_list)
alpha_list.sort()
print(alpha_list)
sorted_list = alpha_list.sort()
print(sorted_list)  # this prints None as sorting mechanism in lists just sorts the original list in place and update the original list
                    # itself but the sorted list can't be assigned to any other variable
                    


                                                                      # --: TUPLES :- #

# A tuple is similar to a list, but you create them with parentheses instead of square brackets. You can
# also use the tuple built-in. The main difference is that a tuple is immutable while the list is mutable.
# Let’s take a look at a few examples:

my_tuple = (1,2,3)
print(my_tuple[0:3])
another_tuple = tuple() # It is an empty tuple
abc_tuple = tuple((1,2,3))
print(abc_tuple)
list_to_tuple = tuple([1,2,3]) # Here we passed a list argumnet to tuple function. Now the list type will be casted into Tuple type
print(list_to_tuple)
# We can convert above tuple into list back we can do as shown below
tuple_to_list = list(list_to_tuple)
print(tuple_to_list)


                                                             # --: DICTIONARIES :- #
        
# A Python dictionary is basically a hash table or a hash mapping. In some languages, they might be
# referred to as associative memories or associative arrays. They are indexed with keys, which can
# be any immutable type. For example, a string or number can be a key. You need to be aware that a
# dictionary is an unordered set of key:value pairs and the keys must be unique. You can get a list of
# keys by calling a dictionary instance’s keys method. To check if a dictionary has a key, you can use
# Python’s in keyword. In some of the older versions of Python (2.3 and older to be specific), you will
# see the has_key keyword used for testing if a key is in a dictionary. This keyword is deprecated in
# Python 2.x and removed entirely from Python 3.x


# Below the first two examples show how to create an empty dictionary. All dictionaries are enclosed with
# curly braces. The last line is printed out so you can see how unordered a dictionary is. Now it’s time
# to find out how to access a value in a dictionary
my_dict = {}
my_dict = dict()
my_other_dict = {1:"one",2:"two",3:"three"}
print(my_other_dict)

# Below is the way to access values in a dictionary by using a key
print(my_other_dict[1])
my_name_dict = {"name":"Shashi","country":"India"}
print(my_name_dict["country"])

# We can check whether a key is present in dictionary by using "in" as shown in below. If the respective key presents in the dictionaty
# it returns True otherwise it returns false
print("name" in my_name_dict) # True
print("1" in my_name_dict) # False

# All the keys list can be checked as shown below
print(my_name_dict.keys())
print(my_other_dict.keys())

