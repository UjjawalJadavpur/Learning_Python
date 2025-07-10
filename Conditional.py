#  if else elif
# if(condition):
#     Statement1
# elif(condition)
#     Statement2
# else:
#     StatementN
# indentation - proper spacing 

age = int(input("Enter your age :  "))
print("Your age is  :  ",age)
if(age >= 18):
    print("can vote & apply for license")
else:
    print("wait till your age reach 18 !")
    
light = input("enter the traffic light color :  ")
print("Your traffic light color is  : ",light)
if(light == "red"):
    print("Color is Red - STOP")
elif(light == "yellow"):
    print("color is Yellow - LOOK Start")
elif(light == "green"):
    print("color is Green - GO GO GO !")
else:
    print("Type only traffic color red. yellow, green")
    

marks = int(input("enter the students marks b/w 0 to 100 :  "))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
elif(marks >= 60 and marks < 70):
    grade = "D"
else:
    grade = "E"

print("Your marks is  :  ",marks)
print("your Grade is  :  ",grade)

number = int(input("enter the number :  "))
if(number % 2 == 0):
    print("EVEN")
else:
    print("ODD")
 
    
first  = int(input("enter your first number   :  "))
second = int(input("enter your second number  :  "))
third  = int(input("enter your third number   :  "))

if(first >= second and first >= third):
    print("first number is largest   : ",first)
elif(second >= third):
    print("second number is largest  : ",second)
else:
    print("third number is largest   : ",third)
   
    
print("To check multiple of 7")
x = int(input("Enter your number  :  "))

if(x % 7 == 0):
    print("Yes, it is Multiple of  7 ")
else:
    print("Not a multiple of 7")
