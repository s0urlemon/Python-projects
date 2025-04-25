print("Half-pyramid pattern of stars '✦'")
n=int(input("enter the number of rows you want the stars to be printed:"))
for i in range(n):
    for j in range(n-i):
        print("✦",end=" ")
    print()