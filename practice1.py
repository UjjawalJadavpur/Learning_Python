# excape sequence \t \n 
str1 = "This is a string. We are creating in Python"
print(str1)
str2 = "This is a string.\tWe are creating in Python"
print(str2)
str3 = "This is a string.\nWe are creating in Python"
print(str3)

#concatenation 

str4 = "hello"
print(len(str4))
str5 = "world"
print(len(str5))
print(str4 + str5)
str6 = str4 + str5
print(str6)
print(len(str6))
str7 = str4 + " " + str5
print(str7)
print(len(str7))

# indexing
str8 = "Khan_Global_Studies"
print(str8[2])
# str8[3] = " " not allowed

#slicing - Accesing parts of string
print(str8[1:4])
print(str8[5:9])
print(str8[5:])
print(str8[:9])

# negative indexing
print(str8[-6:-1])
print(str8[-6:])

# string functions 
# ends with 
strr = "i am an Indian"
print(strr.endswith("aa"))
print(strr.endswith("an"))
print(strr.capitalize())
# original string will not change
print(strr)
print(strr.replace("a","K"))
print(strr)
print(strr.find("a"))
print(strr.find("an"))
print(strr.find("z"))
print(strr.count("an"))
print(strr.count("a"))

name = input("enter your name : ")
print("Welcome ",name)
print("length of your name is  ",len(name))

dollar_str = "hi, $ I am the $ symbol $94.99"
print(dollar_str)
print("No of $ in the string : ",dollar_str.count("$")); 
