with open("demo3.txt","r") as f:
    data = f.read()
    print(data)

num = ""
count = 0
for i in range(len(data)):
    if(data[i] == ","):
        # print(int(num))
        if int(num) % 2 == 0:
            print(f"{int(num)} is even")
            count += 1
        else:
            print(f"{int(num)} is odd")
        num = ""
    else:
        num = num + data[i]
        
print("total even no is : ",count)

# nums = data.split(",")