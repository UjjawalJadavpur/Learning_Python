# repeat instructions

count = 1

while count <= 5:
    print("hello",count)
    count = count + 1
    
while count <= 9:
    print("world",count)
    count = count + 1
    
n = int(input("enter the number for multiplication table  : "))
i=0
while i<11 :
    print(n*i)
    i = i+1
    
m = int(input("Enter the number for multiplication table: "))
i = 1
while i <= 10:
    print(f"{m} * {i} = {m * i}")
    i += 1

print("prinitng sqaure of number")

list1 = []
j=0
while j<11:
    k = j*j
    list1.append(k)
    print(k)
    j = j+1 
    
print(list1)

tup1 = (list1)
print(tup1)

w = int(input("enter number to find : "))

y=0
found = False
while y<len(list1)-1:
    print("finding....",y)
    if list1[y] == w:
        print("found at index : ",y)
        found = True
        break
    y = y+1 
    
if( not found):
    print("Not found")
    

l = 0
while l<= 10:
    if l%2 == 0 :
        l = l+1
        continue
    print(l)
    l = l+1

