# built in data types that stores set of values
# store elements of different types (integer,  float, string)

marks = [94.4, 87.5, 95.2, 66.4, 40]
print(marks)
print(type(marks))
print(len(marks))

student = ["karan", 15, 97.5, "Delhi"]
print(student)
print(student[0])
print(student[2])

student[0] = "Arjun"

print(student)

# string is immutable but list is mutable

# slicing in list
print(marks[1:4])
print(marks[-3:-1])
print(marks[-3:])


# list methods

marks.append(55)
print(marks)
print(marks.sort())
# original list changed
print(marks)
print(marks.sort(reverse=True))
print(marks)

list = ["banana", "litch", "apple"]
print(list)
print(list.sort())
print(list)
list.append("orange")
print(list)
print(list.sort())
print(list)
list.append("kiwi")
print(list)
print(list.sort())
print(list)
print(list.reverse())
print(list)

list.insert(1,"peach")
print(list)
list.remove("kiwi")
print(list)
list.pop(3)
print(list)

# Tuples - built in data type - immutable sequences of values

tup = (87,64,33,95,76,33,33)

# tup[0] = 43 not allowed
print(type(tup))
print(tup)
print(tup[0])

print(tup[1:3])
print(tup[1:])

print(tup.index(33))
print(tup.count(33))

movies = []
mov = input("enter 1st movies :  ")
movies.append(mov)
mov = input("enter 2nd movies :  ")
movies.append(mov)
movies.append(input("enter 3rd movies :  "))

print(movies)

list1 = [1,2,3,2,1,3]
copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("pallindrome")
else:
    print("Not Pallindrome")

list1 = [1, 2, 3, 2, 1, 3]

# Manually create a reversed copy
copy_list1 = []
for i in range(len(list1) - 1, -1, -1):
    copy_list1.append(list1[i])

# Manually compare elements
is_palindrome = True
for i in range(len(list1)):
    if list1[i] != copy_list1[i]:
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")


grade = ("C", "D", "A", "A", "B", "B", "A")
print(grade)
print(type(grade))
print("Count of  A : - ",grade.count("A"))

# Convert to list
grade_list = []
for item in grade:
    grade_list.append(item)

# Sort the list (manually, without built-in sort)
for i in range(len(grade_list)):
    for j in range(i + 1, len(grade_list)):
        if grade_list[i] > grade_list[j]:
            grade_list[i], grade_list[j] = grade_list[j], grade_list[i]

# Print the sorted list
print("Sorted Grade List:", grade_list)
print("Type after conversion:", type(grade_list))