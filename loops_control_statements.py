#break statement
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 3:
        break
    print(number) #Stops printing when it get's to 3
    
#continue statement
number_two = [6, 7, 8, 9, 10]
for number in number_two:
    if number == 9: # Skips at 9 and contintues
        continue
    print(number)