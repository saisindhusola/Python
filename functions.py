#Assigning a variables
caluclation_to_units = 24 * 60 * 60
name_of_unit = "seconds"
print(f"2 days are {2 * caluclation_to_units} {name_of_unit}")

#Creating a function
def days_to_units():
    print(f"2 days are {2 * caluclation_to_units} seconds.")
    print("Hello!How are you?")
days_to_units()

#Passing Parameters
def days_to_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days * caluclation_to_units} seconds.")
    print("Hello!How are you?")
days_to_units(2)
days_to_units(3)
days_to_units(4)
days_to_units(5)

#Passing more arguments
def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * caluclation_to_units} seconds.")
    print(custom_message)
days_to_units(2,"fine!")
days_to_units(3,"Looks good!")

#Variable scopes in function
def scope_check(count_of_day):
    my_var = "variable inside function" #local variable declared inside the function.
    print(name_of_unit) #Global variable declared outside the function.
    print(count_of_day) #Argument passed to parameter.
    print(my_var)
    #print(num_of_days) #doesn't execute because it is local variable declared in the above function.
    
scope_check(20)
