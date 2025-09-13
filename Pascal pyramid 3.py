n = int(input("Enter n : "))

for i in range(n):
    for j in range(n-i-1):
        print(format("", "<2"),end="")
    num=1
    for j in range(i+1):
        print(format(num,"<4"),end="")
        num = num * (i-j) // (j+1)
    print()