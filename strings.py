#Data Types #Strings

#String Split
arn = "Hello,Welcome to DevOps Class. Enjoy/learning!"
print(arn.split("/")[0])
splittext = "Python is Awesome"
words = splittext.split()
print("words:", words)


#String Conversion
name = "sindhu"
print(name.upper()) #Converts to Uppercase
text = "Enjoy Learning Python"
uppercase = text.upper()
lowercase = text.lower()
print("Uppercase: ", uppercase)
print("Lowercase: ", lowercase)

#Adding two strings - String Concatenation
str1 = "Hello"
str2 = "World"
one = (str1+str2) #without Space
two = (str1+" "+str2) #with Space
result = str1+" "+str2
print(one,two)
print(result)

#Length of the String
name = "Sai Sindhu Sola"
length = len(name)
print("Length of the string is:", length)

#String Replace
first = "Enjoy Learning Python"
later = first.replace("Enjoy", "Have fun")
print(later)

#String Strip
striptext ="  Python is Awesome  " #Removes extra spaces
newstrip = striptext.strip()
print("Stripped text:", newstrip)

#Substring
subtext = "Python is awesome"
substring = "is"
if substring in subtext:
    print(substring, "found in text")