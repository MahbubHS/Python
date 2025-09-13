n = int(input("Number of row: "))
col = n+n-5
mid = col//2
for i in range(n):
    for j in range(col):
        if j==2 or j==(n-3) or i+j==mid or j-i==mid or i-j==2 or i+j==(col+1):
            print("*", end="")
        else:
            print(" ", end="")
    print()
