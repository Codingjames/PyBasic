import turtle
import random
t = turtle.Pen()
t.shape("turtle")
t.speed(200)
t.color("black")
t.screen.bgcolor("black")
f = 100
for x in range(100):
  
    t.pencolor(random.random(), random.random(), random.random())
    t.forward(200)
    t.right(160)
    for i in range(10):
        t.circle(30,15)
    for i in range(10):
        t.circle(-30,-15)
    if(x%10==0):
        f+=20
        t.color(random.random(), random.random(), random.random())
    # t.right(190)
    t.forward(f)
# t.back(150)
# x=-2
# y=-2
# for i in range(100):
#     t.pencolor("red")
#     if(i%10==0):
#         # t.goto(x,y)
#         t.forward(50)
#         t.left(10)
     
#     c+=1
#     t.circle(40)
#     t.right(c)
#     t.forward(50)
#     # t.right(120)
    
turtle.mainloop()