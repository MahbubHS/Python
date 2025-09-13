num = int(input("Enter rows : "))
row = 0

while row<num:
    space = num - row - 1
    while space>0:
        print(end=" ")
        space -=1
    star = row +1
    while star>0:
        print("*", end=" ")
        star-=1
    row +=1
    print()
