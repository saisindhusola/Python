my_Set = {1, 2, 3, 4, 5}
my_Set.add(6) #Adding elements to the Set.
my_Set.remove(1)#Removing element from the set.
print(my_Set)

#Set Operations
set_One = {1, 2, 3, 4, 5, 6}
set_Two = {5, 6, 7, 8, 9, 10}
union_Set = set_One.union(set_Two)
intersection_Set = set_One.intersection(set_Two)
difference_Set = set_One.difference(set_Two)

print(union_Set)
print(intersection_Set)
print(difference_Set)

#Subset and Superset
is_Subset = set_One.issubset(set_Two) #Checks if setOne is subset of setTwo.
is_Superset =set_One.issuperset(set_Two) #Checks if setOne is superset of setTwo.
print(is_Subset)
print(is_Superset)