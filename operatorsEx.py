#Arithmetic Operators
a = 2
b = 4
addition = a + b
sub = a-b
product = a * b
quotient = a / b
print("Sum of a and b is: ", addition)
print("Subtraction : ", sub)
print("Product of a and b is: ", product)
print("Quotient : ", quotient)

#Comparision Operators
c = 22
d = 19
greater_Value = c > d
less_Value = c < d
less_Equal = c <= d
greater_Equal = c >= d
equal_To = c == d
not_Equal = c != d
print("Greater Value: ", greater_Value)
print("Lessthan sum: ", less_Value)
print("Less than equal: ", less_Equal)
print("Greater than equal: ", greater_Equal)
print("Equal to: ", equal_To)
print("Not equal: ", not_Equal)

#Logical Operators
x = True
y = False

and_Result = x and y
or_Result = x or y
not_ResultX = not x
not_ResultY = not y

print("AND result: ", and_Result)
print("OR result: ", or_Result)
print("NOT Result of X: ", not_ResultX)
print("NOT Result of Y: ", not_ResultY)


my_list = [1, 2, 4, 5, 6]

# Identity operators
a = my_list
b = [1, 2, 4, 5, 6]

is_same_object = a is my_list
is_not_same_object = b is not my_list

# Membership operators
element_in_list = 3 in my_list
element_not_in_list = 6 not in my_list

print("a is my_list:", is_same_object)
print("b is not my_list:", is_not_same_object)
print("3 in my_list:", element_in_list)
print("6 not in my_list:", element_not_in_list)
