"""
# Using Generator Functions
def count_up_to(max):
 counter = 1
 while counter <= max:
  yield counter
  counter += 1
# Using the generator function
gen = count_up_to(5)
for number in gen:
 print(number) """


"""
#Using Generator Expressions
gen = (x ** 2 for x in range(5))
for number in gen:
 print(number)
"""

"""
#: Generate only even numbers from a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = (x for x in numbers if x % 2 == 0)
for even in evens:
 print(even) """

"""# Convert all the strings in a list to uppercase:
words = ["hello", "world", "python", "generators"]
uppercase_words = (word.upper() for word in words)
for word in uppercase_words:
 print(word)  """

"""
#Using Iterators
# Define a list (which is an iterable)
numbers = [1, 2, 3, 4, 5]
# Get an iterator from the list
iterator = iter(numbers)
# Access elements using the iterator
print(next(iterator)) # Output: 1
print(next(iterator)) # Output: 2
print(next(iterator)) # Output: 3    """

"""#Infinite Iterators
def infinite_count(start=0):
 while True:
  yield start
  start += 1
# Create an infinite iterator
counter = infinite_count()
# Get the first 5 numbers
for _ in range(5):
 print(next(counter))"""

"""
# Iterator with a List
# Define a list (an iterable)
fruits = ['apple', 'banana', 'cherry']
# Get an iterator using the iter() function
fruit_iterator = iter(fruits)
# Access elements one by one using next()
print(next(fruit_iterator)) # Output: apple
print(next(fruit_iterator)) # Output: banana
print(next(fruit_iterator)) # Output: cherry   """


"""
# Iterator with a Dictionary
# Define a dictionary (an iterable)
person = {'name': 'John', 'age': 30, 'city': 'New York'}
# Get an iterator over the keys using the iter() function
key_iterator = iter(person)
# Access keys one by one using next()
print(next(key_iterator)) # Output: name
print(next(key_iterator)) # Output: age
print(next(key_iterator)) # Output: city"""


"""
#Use a generator to manage user inputs dynamically
def user_input_generator():
 while True:
  command = input("Enter a command (type 'exit' to quit): ")
  if command.lower() == 'exit':
   break
  yield command
# Usage
def process_commands():
 for command in user_input_generator():
  print(f"Executing command: {command}")
process_commands()    """


"""
#Use a generator to filter data without loading the entire dataset into memory.
def filter_large_dataset(dataset, criterion):
 for item in dataset:
  if criterion(item):
   yield item
# Example dataset
large_dataset = range(100)
# Usage
def print_filtered_data():
 for item in filter_large_dataset(large_dataset, lambda x: x % 2 == 0):
  print(item,end=' ')
print_filtered_data()  """



"""import sys
data=[i for i in range(1,100)]
print(data)
print(sys.getsizeof(data[0]))"""



"""data=(i for i in range(1,100))
for i in data:
    print(i)
print(sys.getsizeof(data))"""


"""def listofval():
    i=0
    while i<100:
        i+=1
        yield i
x=listofval()

for i in x:
    print(i)  """


"""list1=[i for i in range(200)]
data=iter(list1)
print(data._next_())
print(data._next_())
print(data._next_())
print(next(data))"""


"""
def log_file_reader(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Usage
def analyze_logs(file_path):
    for line in log_file_reader(file_path):
        # Perform analysis on each line
        if "ERROR" in line:
            print(f"Error found: {line}")

analyze_logs('server_logs.txt')   """



"""def user_input_generator():
    while True:
        command = input("Enter a command (type 'exit' to quit): ")
        if command.lower() == 'exit':
            break
        yield command

# Usage
def process_commands():
    for command in user_input_generator():
        print(f"Executing command: {command}")

process_commands()"""

import time
def comm(fun):
    def inner():
        t1=time.time()
        fun()
        t2=time.time()
        print("Time taken",(t2-t1))
    return inner
@comm
def one():
    data1=[]
    for i in range(1,1000000):
        data1.append(i)
@comm
def two():
    data2=[]
    for i in range(1,5000000):
        data2.append(i)

two()






