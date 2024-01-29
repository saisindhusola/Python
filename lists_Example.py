#try following list methods
# append, clear, copy,count, extend, index, insert, pop, remove, reverse, sort.
no_of_People = ['Ram','Seetha','lakshman','Hanu']
print(no_of_People)

# using append to add elements to the list
no_of_People.append('Hanu')
print(no_of_People)

# to copy elements from the list
copy_People = no_of_People.copy()
print(copy_People)

# Clear to empty the list
no_of_People.clear()
print(no_of_People)

# To remove particular elements
copy_People.remove('lakshman')
print(copy_People)

# to count the number ofelements
hanu_Count = copy_People.count('Hanu')
print(hanu_Count)

#to add new list to existing list
new_People = ['Janu', 'Ramu']
copy_People.extend(new_People)
print(copy_People)

#to find out the place of element
print(copy_People)
print(copy_People.index('Janu'))

#to insert element at particular location
copy_People.insert(2, 'Lavkush')
print(copy_People)

#pop to remove an element
copy_People.pop() # if no value passed, removes last element by default
print(copy_People)
copy_People.pop(3)
print(copy_People)

#Similar to pop, remove is used to delete the element
copy_People.remove('Janu')
print(copy_People)

#Sort is used to get list in orderly manner
copy_People.sort() #gives list is alphabetic order
print(copy_People)

#to reverse the list
copy_People.reverse()
print(copy_People)