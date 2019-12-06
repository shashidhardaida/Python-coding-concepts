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