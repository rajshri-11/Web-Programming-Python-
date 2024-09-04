"""Example 1:
# dictionary comprehension example
square_dict = {num: num*num for num in range(1, 11)}
print(square_dict)
#output:{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
"""

"""Example 2:
#item price in dollars
old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}
dollar_to_pound = 0.76
new_price = {item: value*dollar_to_pound for (item, value) in old_price.items()}
print(new_price)
#output:{'milk': 0.7752, 'coffee': 1.9, 'bread': 1.9}   """


"""Example 3:
#Conditionals in Dictionary Comprehension
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
even_dict = {k: v for (k, v) in original_dict.items() if v % 2 == 0}
print(even_dict)
#output:{'jack': 38, 'michael': 48}    """


"""Example :4
#Multiple if Conditional Dictionary Comprehension
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
new_dict = {k: v for (k, v) in original_dict.items() if v % 2 != 0 if v < 40}
print(new_dict)

#output:{'john': 33}  """

"""Example :5
 #if-else Conditional Dictionary Comprehension
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

new_dict_1 = {k: ('old' if v > 40 else 'young')
    for (k, v) in original_dict.items()}
print(new_dict_1)

#output:{'jack': 'young', 'michael': 'old', 'guido': 'old', 'john': 'young'}
"""


"""Example :5
#Nested Dictionary with Two Dictionary Comprehensions
dictionary = {
    k1: {k2: k1 * k2 for k2 in range(1, 6)} for k1 in range(2, 5)
}
print(dictionary)

#output:{2: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}, 3: {1: 3, 2: 6, 3: 9, 4: 12, 5: 15}, 4: {1: 4, 2: 8, 3: 12, 4: 16, 5: 20}}
"""

"""Example :6
#Square of Numbers
squares = {x: x**2 for x in range(1, 6)}
print(squares)
#output:{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}   """


"""Example :7
#Filtering Even Numbers
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)
#output:{2: 4, 4: 16, 6: 36, 8: 64, 10: 100}   """


"""Example :8
#Nested Dictionary Comprehension
nested_dict = {x: {y: y**2 for y in range(1, 4)} for x in range(1, 4)}
print(nested_dict)
#output:{1: {1: 1, 2: 4, 3: 9}, 2: {1: 1, 2: 4, 3: 9}, 3: {1: 1, 2: 4, 3: 9}}
"""


"""Example :9
#Inverting a Dictionary
original_dict = {'a': 1, 'b': 2, 'c': 3}
inverted_dict = {v: k for k, v in original_dict.items()}
print(inverted_dict)
#output: {1: 'a', 2: 'b', 3: 'c'}     """


#Example :10
#Creating a Dictionary from Two Lists
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']
person_dict = {k: v for k, v in zip(keys, values)}
print(person_dict)
#output:{'name': 'Alice', 'age': 25, 'city': 'New York'}




























































