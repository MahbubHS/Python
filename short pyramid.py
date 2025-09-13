n = int(input("Enter n : "))

for i in range(n+1):
    print(" "*(n-i),end="")
    print(("*"+" ")*i)