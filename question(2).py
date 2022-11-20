num=int(input("enter num:"))
for i in range(0,num+1):
    for j in range(num-i,0,-1):
        print(j,end=" ")
    print(" ")