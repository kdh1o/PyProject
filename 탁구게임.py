from turtle import Turtle, Screen
import time
import random

#창설정
win=Screen()
win.title("탁구게임")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)

#판그리기
t=Turtle()
t.speed("fastest")
t.penup()
t.color("white")
t.goto(320,320)
t.pensize(3)
t.pendown()
t.setheading(180)
for i in range(4):
    t.fd(640)
    t.left(90)
t.hideturtle() 

#플레이어 정의
player=Turtle()
player.penup()
player.speed("fastest")
player.color("gray")
player.shape("square")
player.shapesize(1,6)
player.goto(0,-260)

#점수판
score=0
p=Turtle()
p.color("white")
p.speed("fastest")
p.hideturtle()
p.penup()
p.goto(-430,250)
p.pendown()
p.write("Score:%d"% score, font=("@Fixedsys", 20, "normal"))

#목숨
life=3
l=Turtle()
l.color("white")
l.speed("fastest")
l.hideturtle()
l.penup()
l.goto(-430,220)
l.pendown()
l.write("Life:%d"% life, font=("@Fixedsys", 20, "normal"))

#공
b=Turtle()
b.color("white")
b.shape("circle")
b.penup()
b.direction="stop"

#함수정의
def left():
    if player.xcor()>-250:
        player.backward(50)
    win.update()

def right():
    if player.xcor()<250:
        player.fd(50)
    win.update()


#함수실행
win.onkeypress(left,"Left")
win.onkeypress(right,"Right")
win.onkeypress(left,"a")
win.onkeypress(right,"d")
win.listen()

bx=0.4
by=0.6

time.sleep(2)

gameon=True
while gameon:
    
    win.update()
    b.setx(b.xcor()+bx)
    b.sety(b.ycor()+by)
        
    #공 벽에 튕기기
    if b.xcor()<-300:
        bx*=-1
    elif b.xcor()>300:
        bx*=-1

    #죽음
    if b.ycor()<-300:
        time.sleep(1)
        b.goto(0,0)
        b.direction="stop"
        by*=-1
        bx*=-1
        player.goto(0,-260)
        life-=1;
        l.clear()
        l.write("Life:%d"% life, font=("@Fixedsys", 20, "normal"))
               
    elif b.ycor()>300:
        by*=-1

    #플레이어 충돌
    if(player.xcor()-50<b.xcor()<player.xcor()+50) and (-250<b.ycor()<-240):
        by*=-1
        score+=10
        p.clear()
        p.write("Score:%d"% score, font=("@Fixedsys", 20, "normal"))

    #게임끝
    if life==0:
        p.penup()
        p.goto(-100,0)
        player.hideturtle()
        b.hideturtle()
        p.write("Game Over", font=("@Fixedsys", 40, "normal"))
        gameon=False

    
win.update()
win.mainloop()





