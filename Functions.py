# block of statement that perform specific task

# def fun_name (arg):
#   return val
# fun_name(arg)

# default parameter - which is used when no argument is passed
# first non default then default
def cal_sum(a,b=2):
    print(a+b)
    
cal_sum(1,4)

city = ["delhi", "patna", "kolkata"]
hero = ["thor", 2,"ironman",3,4,6]

def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item, end=" ")
    
print_len(city)
print_len(hero)

print_list(city)
print()
print_list(hero)
print()

def cal_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    print(f"factorial of {n} is : ",fact)
    return fact

def cal_fact_recursion(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n* cal_fact_recursion(n-1)
    
z = int(input("enter the n for factorial : "))

print(f"factorial of {z} is : ",cal_fact(z))
print(f"factorial of {z} is : ",cal_fact_recursion(z))


# Recursion - function which calls itself repeatedly

def show(n):
    if n==0 :
        return
    print(n)
    show(n-1)
    
show(5)

def cal_sum_rec(n):
    if n == 0:
        return 0
    return n + cal_sum_rec(n-1)

print("Recursive sum of 10 is : ",cal_sum_rec(10))

def print_list_rec(list,idx = 0):
    if(idx == len(list)):
        return
    print(list[idx])
    return print_list_rec(list, idx+1)

print_list_rec(hero)