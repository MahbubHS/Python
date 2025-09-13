from turtle import *

speed(100)
bgcolor('black')
color('green')
hideturtle()

n=1
p= True

while True:
    circle(n)
    if p:
        n-=1
    else:
        n+=1
    if n==0 or n==30:
        p= not p
    left(3)
    right(2)
    forward(5)