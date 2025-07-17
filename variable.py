def greet():
    msg = "Hello from inside the function!"
    print(msg)

greet()
msg = "Python is awesome!"

def display():
    print("Inside function:", msg)

display()
print("Outside function:", msg)


s = "I love Geeksforgeeks"
print(s)
def fun():
    s = "Me too."
    print(s)
fun()   
print(s)

def fun():
    global s
    s += ' GFG'   # Modify the global variable
    print(s)
    s = "Look for Geeksforgeeks Python Section"
    print(s)

s = "Python is great!"
fun()
print(s)

a = 1  # Global variable

def f():
    print('f():', a)  # Uses global a

def g():
    a = 2  # Local variable shadows global
    print('g():', a)

def h():
    global a
    a = 3  # Modifies global a
    print('h():', a)

print('global:', a)  
f()                  
print('global:', a) 
g()                 
print('global:', a)  
h()                  
print('global:', a)