# Lists

# 1. Create a list
numbers = [1, 2, 3, 4]
print('Create a list: ', numbers)  # [1, 2, 3, 4]

# 2. Access list items
print('Access list items: ', numbers[2])  # [3]

# 3. Change the value of a list item
print('Changed index 2: ', numbers[2] + 3)  # [6]

# 4. Loop through a list
for x in numbers:
    print(f'Looping through a list: {x}')

# 5. Check if a list item exists
if 2 in numbers:
    print('2 is in the list numbers')

# 6. Get the length of a list
print(f'The length of the list numbers: {len(numbers)}')

# 7. Add an item to the end of a list
print(f'Appended a 5 to end of list: {numbers.append(5)}')

# 8. Add an item at a specified index
numbers.insert(2, 333)
print(f'Added 333 to index 2: {numbers}')

# 9. Remove an item
print(f'Removed 5 from the end: {numbers.pop()}')

# 10. Remove an item at a specified index
print(f'Removed 333 from index 2: {numbers.pop(2)}')

# 11. Empty a list
print(f'Empty a list: {numbers.clear()}')

# 12. Use the list() constructor to make a list
colors = list()
print(f'Constrcted colors list: {colors}')

# Dictionaries

# 1. Create a dictionary
person1 = {
    'name': 'Brianna',
    'age': 25
}
print('New dictionary: ', person1)

# 2. Access the items of a dictionary
print('Access name of dictionary: ', person1['name'])

# 3. Change the value of a specific item in a dictionary
person1['name'] = 'Brianna Keune'
print('Changed name to be full name: ', person1['name'])

# 4. Print all key names in a dictionary, one by one
for key in person1:
    print('Key names of person1: ', key)

# 5. Print all values in a dictionary, one by one
for value in person1.values():
    print('Values of person1: ', value)

# 6. Use the values() function to return values of a dictionary
print('Values of person1 not in a loop: ', person1.values())

# 7. Loop through both keys and values, by using the items() function
for key, value in person1.items():
    print('Items of person1: ', key, value)

# 8. Check if a key exists
if 'name' in person1:
    print('Name exists: ', person1['name'])

# 9. Get the length of a dictionary
print('Length of dict: ', len(person1))

# 10. Add an item to a dictionary
person1['fav_color'] = 'yellow'
print('Added fav_color to person1: ', person1)

# 11. Remove an item from a dictionary
try:
    del person1['fav_color']
    print('Deleted fav_color', person1)
except KeyError:
    print("Key 'fav_color' does not exist")

# 12. Empty a dictionary
print('Empty person1 dictionary: ', person1.clear())

# 13. Use the dict() constructor to create a dictionary
randomDict = dict()
print("New dictionary: ", randomDict)

# Tuples

# 1. Create a tuple
my_first_tuple = ('Brianna', 'Keune', 25, 'Wisconsin')
print('created tuple: ', my_first_tuple)
# 2. Access tuple items
print('accessing index 1 of tuple: ', my_first_tuple[1])  # Keune

# 3. Change tuple values
# tuple values are immutable...
tmplist = list(my_first_tuple)
tmplist[1] = "K"
my_first_tuple = tuple(tmplist)
print('Updated tuple value at 1: ', my_first_tuple)  # K

# 4. Loop through a tuple
for x in my_first_tuple:
    print('Looping through tuple: ', x)

# 5. Check if a tuple item exists
if 'Wisconsin' in my_first_tuple:
    print('Wisconsin is in my first tuple.')

# 6. Get the length of a tuple
print('Length of myfirsttuple: ', len(my_first_tuple))

# 7. Delete a tuple
try:
    del my_first_tuple
    print('Deleted my_first_tuple')
except KeyError:
    print('my_first_tuple does not exist')

# 8. Use the tuple() constructor to create a tuple
new_tuple = tuple(["Happy", "Birthday", "Frosty"])
print('Used tuple constructor: ', new_tuple)

# Sets

# 1. Create a set
movies = {'Finding Nemo', 'Aladdin', 'Onward'}
print('created a set movies: ', movies)

# 2. Loop through a set
for x in movies:
    print("Looping through set: ", movies)

# 3. Check if an item exists
if 'Aladdin' in movies:
    print('Aladding is in movies')

# 4. Add an item to a set
movies.add('Big Hero 6')
print('Added a new movie: ', movies)

# 5. Add multiple items to a set
movies.update(['The Princess Bride', 'Shrek'])
print('Added multiple items to set: ', movies)

# 6. Get the length of a set
print('Length of movies: ', len(movies))

# 7. Remove an item in a set
try:
    movies.remove('Shrek')
    print('Shrek was deleted from movies.')
except KeyError:
    print('Shrek was not found.')

# 8. Remove an item in a set by using the discard() method
movies.discard('The Princess Bride')
print('The Princess Bride was removed from movies: ', movies)

# 9. Remove the last item in a set by using the pop() method
print(movies.pop(), "Removed last item from movies")

# 10. Empty a set
movies.clear()
print('Cleared movies: ', movies)

# 11. Delete a set
try:
    del movies
    print('Deleted movies set')
except KeyError:
    print('movies set not found.')

# 12. Use the set() constructor to create a set
new_set = set(["red", "yellow", "pink"])
print('constrcted new set: ', new_set)
