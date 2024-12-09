## LIST
fruits_list = ['apple','banana','grapes'] # we can set a list of strings
numbers = [1, 2, 3, 4, 5] # a list of numbers
mixed_list = ['text', 1, 5.5] # even diferent types of variables

# The order is preserved
# We can acces to the elements by index
# We can modify the content after created

print(fruits_list[0]) # we can acces to an item by his index
print(fruits_list[0:2]) # we slice the elements like a string

fruits_list.append('orange') # we can append elements after created
print(fruits_list)

fruits_list[0] = 'cherry' # we can modify an element
print(fruits_list)

fruits_list.remove('banana') # we can remove elements
print(fruits_list)

print(len(fruits_list)) # we can get the lenght of the list too

## TUPLES
# Tuples are basically list but inmutable and they use '()'

coordinates = (10, 20)
colors = ('red', 'blue', 'green')
single_element = ('one',) # for one element we need to add a comma

# The order is preserved
# We can acces to the elements by index
# We cannot modify the content after created

print(coordinates[0]) # accesing by index
print(coordinates[0:2]) # we can slice too, like a string
print(len(colors)) # we can get the lenght too

# Tuples are faster and memory-efficient than lists
# Commonly used for fixed data or when we wan to preventn data modification

## DICTIONARIES
# In my experience is like a hashmap for Java
# Key-value pairs

person = {"name": "Patricio", "age": "28", "city": "Pucallpa"}

# This structure don't preserver order
# Each value is associated to his key
# We can add, remove o change key-value pairs

print(person["name"]) # we can access to the value by his key

person["age"] = 35 # we can modify the value associated with a key
person["email"] = "example@mail.com" # we can add new key-value pairs
print(person)

del person["city"] # we can remove a key-value pair
print(person)

if "phone" in person: # we can verify if a key exists
    exists_phone = True
else:
    exists_phone = False

print('Key <<phone>> exists?? ' + str(exists_phone))

print(person.keys()) # we can get all the keys
print(person.values()) # we can get all the values

print(len(person)) # and we can get the lenght