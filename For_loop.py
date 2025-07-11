# for loop - sequential traversal  for traversing list string tuples

nums = [1,2,3,4,5,6,7]

for el in nums:
    print(el)

veggies = ["potato", "brinjal", "tomato"]

for val in veggies:
    print(val)
    
tup = (1,2,2,3,4,5)

for el in tup:
    print(el)
    
str = "khan Global Studies"

for char in str:
    print(char)
    

number = [1,4,9,16,25]
x = 9
idx = 0
for el in number:
    if(el == x):
        print("found at idx",idx)
        break
    idx = idx+1
    
    
# range function - return a sequence of numbers, starting from 0 by default,
# increment by 1 , stops before a specified number
# range(start? , stop, step?)

print(range(5))

seq = range(10)
print(seq[0])
print(seq[2])
print(seq[4])
print(seq[6])

for ele in seq:
    print(ele)

for el in range(2,10):
    print(el)

for el in range(2,10,3):
    print(el)

z = int(input("enter the n : "))

for el in range(1,11):
    print(z*el)
    
# pass statement - null statement that does nothing
# used as placeholder for future code

for i in range(5):
    pass
print("some work")

sum = 0
z = int(input("enter first  n natural no : "))
for i in range(1,z+1):
    sum = sum + i
print(f"sum of first {z} natural number ",sum)

fact = 1
z = int(input("enter the n for factorial : "))

for i in range(1,z+1):
    fact = fact*i
print(f"factorial of {z} is : ",fact)