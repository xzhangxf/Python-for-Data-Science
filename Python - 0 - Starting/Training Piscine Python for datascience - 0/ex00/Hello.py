ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# Modify the strings
ft_list[1] = "World!"
ft_tuple = (ft_tuple[0], "Singapore!")
ft_set.remove("tutu!")
ft_set.add("Singapore!")
ft_dict["Hello"] = "42Singapore!"

# Print the modified data objects
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

# 1. List
# A list is a collection of items that are:
#       Ordered: The order you put items in is preserved.
#       Mutable: You can change, add, or remove items.
#       Allows duplicates.
# 2. Tuple
#   A tuple is like a list, but:
#       Ordered
#       Immutable: You cannot change it after it’s created.
#       Allows duplicates
# 3. Set
#   A set is a collection of unique items that are:
#       Unordered: The order of items is not preserved.
#       Mutable: You can add or remove items.
#       Does not allow duplicates.
# 4. Dictionary
#   A dictionary is a collection of key-value pairs that are:
#       Unordered: The order of items is not preserved.
#       Mutable: You can change, add, or remove items.
#       Keys must be unique, but values can be duplicated.
#       Allows for fast lookups by key.
