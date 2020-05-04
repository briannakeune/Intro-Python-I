# Lists

# 1. Create a list
numbers = [1, 2, 3, 4]
print('Create a list: ', numbers) # [1, 2, 3, 4]

# 2. Access list items
print('Access list items: ', numbers[2]) #[3]

# 3. Change the value of a list item
print('Changed index 2: ', numbers[2] + 3) #[6]

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
# 2. Access the items of a dictionary
# 3. Change the value of a specific item in a dictionary
# 4. Print all key names in a dictionary, one by one
# 5. Print all values in a dictionary, one by one
# 6. Use the values() function to return values of a dictionary
# 7. Loop through both keys and values, by using the items() function
# 8. Check if a key exists
# 9. Get the length of a dictionary
# 10. Add an item to a dictionary
# 11. Remove an item from a dictionary
# 12. Empty a dictionary
# 13. Use the dict() constructor to create a dictionary

# Tuples

# 1. Create a tuple
# 2. Access tuple items
# 3. Change tuple values
# 4. Loop through a tuple
# 5. Check if a tuple item exists
# 6. Get the length of a tuple
# 7. Delete a tuple
# 8. Use the tuple() constructor to create a tuple

# Sets

# 1. Create a set
# 2. Loop through a set
# 3. Check if an item exists
# 4. Add an item to a set
# 5. Add multiple items to a set
# 6. Get the length of a set
# 7. Remove an item in a set
# 8. Remove an item in a set by using the discard() method
# 9. Remove the last item in a set by using the pop() method
# 10. Empty a set
# 11. Delete a set
# 12. Use the set() constructor to create a set