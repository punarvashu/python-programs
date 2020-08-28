#Exercise 4

print("How Many Row You Want To Print")
n = int(input())
print("Type 1 for true and 0 for false")
choice = int(input())
new =bool(choice)
if new == True:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print(" ")
elif new ==False:
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print("*", end="")
        print(" ")