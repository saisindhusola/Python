#Functions practice

#Program without funtion to print sum of addition, subtraction and multiplication.
numOne = 20
numTwo = 8

additionOne = numOne + numTwo
print(additionOne)

SubtractionOne = numOne - numTwo
print(SubtractionOne)

multiplicationOne = numOne * numTwo
print(multiplicationOne)


#Program with function to print sum of addition, subtraction and multiplication.
#Advantage of using functions is code readability, reusability(Modularity), easy debugging

numThree = 14
numFour = 7

def addition():
    add = (numThree + numFour)
    print(add)
def subtraction():
    sub = (numThree - numFour)
    print(sub)
def multiplication():
    mul = (numThree * numFour)
    print(mul)
addition()
subtraction()
multiplication()
