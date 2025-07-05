#Functions are a fundemental way to structure your code in Python. they allow you to encapsulate a code and reuse it throughout your program, which leads to more readable and manageble functions.
# In Python you use the def keyword folled by the function name and then the parentheses
#inside these parenthese you can specify any parameteres that your function should take


def greet(name):
    print(f"Hello, {name}")
    
    greet("Siyanda")
    
    
def add(a, b):
    return a + b

result = add(2, 5)
print(result)


def factorial(n):
    if n == 0:
       return 1
   else:
       return n*factorial(n-1)
   
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")
    
greet("Siyanda", "Howzit")
   
   



