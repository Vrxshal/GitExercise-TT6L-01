import random

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)
print("Random number:", random_number)

# Generate a random floating-point number between 0 and 1
random_float = random.random()
print("Random float:", random_float)

# Generate a random element from a list
my_list = ["apple", "banana", "cherry", "date"]
random_element = random.choice(my_list)
print("Random element from list:", random_element)
