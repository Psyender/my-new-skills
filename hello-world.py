#lesson1
print("hello worldish")


#strings lesson2
message = "hello world"
#when theres an apostrophy we add single quotes

print(message)

#advanced concepts-strings

message = 'hello'

print(message[0])
print(message[3])
print(len(message))


message = 'hello world how are we'

print(message.strip())  #Remove leading and trailing whitespace
print(message.lower()) #convert all characters to lowercases
print(message.split(',')) # split the string into a list based on the comma

#tryout upper method
#replace method

#Variables

my_variable = 10
total_count = 0
user = 'John'

#invalid
second_variable = 10 # underscore not a dash


#Operators
#Addition(+)
#Subtraction(-)
#Multiplication(*)
#Division(/)
#Modulus(%)
#Exponent(**)
  
  
x = 10
y = 2 

print(x+y)
print(x-y)
print(x*y)
print(x-y)
print(x/y)
print(x%y)
print(x**y)

x = 10
x = x + 2
x += 2

print (x)


# Operators with Strings

str1 = 'Hello' 
str2 = 'World'

print(str1 + " " + str2)


# Controll Statements

#If statement- is used to execute a block of codeonly if a specific condition is true

num = 10

if num > 0:
    print("this number is positive")
elif num == 0:
    print("This number is zero")
else:
    print("this number is  negative")

#ElIf statement-allows us to check for multiple conditions one after the other

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

if num1 > num2:
   print(num1, "is greater than", num2)
elif num2 > num1:
    print(num2,"is greater than",num1)
else:
    print("Both numbers are equal")



#Loops

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
    
numbers = [1, 2, 3, 4, 5, 6, 7 ]

for number in numbers:
    print(number)
    
    #using while loop to count from 1 to 5
    count = 1
    
    while count <=5:
        print(count)
        count += 1   # increments the counts by 1
        
        
        fruits = ["apple","banana","cherry","date"]
        
        for fruit in fruits:
            if fruit == "cherry":
                break  #Exit loop if cherry is found
            print (fruit)
            
print()


fruits = ["apple","banana","cherry","date"]
for fruit in fruits:
            if fruit == "cherry":
               continue # skips cherry and moves to  the iteration
            print (fruit)
            
print()
fruits = ["apple","banana","cherry","date"]
        
for fruit in fruits:
            if fruit == "cherry":
              pass # placeholder , no action is needed for cherry
            print (fruit)
            
            
            
            
            
count = 0

while count < 5:
    print(count)
    count += 1
    if count == 3:
        break  # exit loop when count has reached - 3
    

