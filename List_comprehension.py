""" #Example:1
numbers = [1, 2, 3, 4]

# list comprehension to create new list
doubled_numbers = [num * 2 for num in numbers]

print(doubled_numbers)
#OUTPUT=>[2, 4, 6, 8]    """

"""#Example:2
numbers = [1, 2, 3, 4, 5]

# create a new list using list comprehension
square_numbers = [num * num for num in numbers]

print(square_numbers)

# Output: [1, 4, 9, 16, 25]   """

"""
#Example:3
# filtering even numbers from a list
even_numbers = [num for num in range(1, 10) if num % 2 == 0 ]

print(even_numbers)

# Output: [2, 4, 6, 8]  """

"""#Example:4
word = "Python"
vowels = "aeiou"
# find vowel in the string "Python"
result = [char for char in word if char in vowels]
print(result)
# Output: ['o']    """


"""#Example:5
#Conditionals in Python List Comprehension
ans=[i for i in range(8) if i%2!=0]
print(ans)
#output:[1, 3, 5, 7]  """

""" #Example:6
#Nested Conditionals
ans=[i for i in range(8) if i%2==0 if i%3==0]
print(ans)
#output:[0, 6]   """

"""#Example:7
#if..else in List Comprehension
ans=["Even" if i%2==0 else "Odd" for i in range(8)]
print(ans)
#output: ['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']  """


"""#Example:8
#Nested List Comprehension
ans=[[i*j for j in range(1,11)] for i in range(7,9)]
print(ans)
#output:[[7, 14, 21, 28, 35, 42, 49, 56, 63, 70], [8, 16, 24, 32, 40, 48, 56, 64, 72, 80]]

"""

"""#Example:9
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
result=[i.upper() for i in fruits]
print(result)
#output:['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']   """

#Example:10 
data=[i for i in range(1,21)]
ans=[i for i in data if i%2==0 ]
print(ans)
#output:[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]





























