# used to perform operations on a file (read, write data)
# f = open("file_name","mode")

f = open("demo.txt","r")
data = f.read()
print(data)
print(type(data))
f.seek(0)  # Reset file pointer to the beginning
line1 = f.readline()
print(line1)
print(type(line1))
line2 = f.readline()
print(line2)
print(type(line2))
f.close()
  
f = open("demo1.txt", "r")
data = f.read()
print(data)
f.close()

f = open("demo1.txt","w")
f.write("i want to learn python. ")
f.close()


f = open("demo1.txt","a")
f.write("\n what is life ?")
f.close()

f = open("demo2.txt","w")
f.write("what is Asur ?")
f.close()

f = open("demo2.txt","r+")
f.write("abc")
read = f.readline()
print(read)
f.close()

with open ("practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning File I/o\n")
    f.write("using Java.\nI like programming in Java.")
    
with open("practice.txt","r") as f:
    data = f.read()
    
new_data = data.replace("Java","Python")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)
    
def check_for_word(word):
    with open("practice.txt","r") as f:
        data = f.read()
        if word in data :
            print("Found")
        else:
            print("Not Found")
   
        
    
check_for_word("learning")

def check_for_line(word) :
    line_no = 1
    with open("practice.txt","r") as f:
        for line in f:
            if word in line:
                print(f"Found on line {line_no}")
                return line_no
            line_no += 1
    print("Not Found")
    return -1
    
check_for_line("Python")
    
    

        
    