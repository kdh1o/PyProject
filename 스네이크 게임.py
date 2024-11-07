from turtle import Turtle, Screen
import time
import random

s=0#점수
hs=0#최고점수
delay=0.1

win=Screen()
win.title("게임")
win.bgcolor("black")
win.setup(width=1000, height=700)
win.tracer(0)

observer=Turtle()
observer.speed("fastest")
observer.color("white")
observer.penup()
observer.fd(490)
observer.pendown()
observer.pensize(5)
observer.setheading(90)
observer.fd(350)
observer.left(90)
observer.fd(1000)
observer.left(90)
observer.fd(700)
observer.left(90)
observer.fd(1000)
observer.left(90)
observer.fd(350)
observer.hideturtle()


#뱀만들기
t=Turtle()#뱀
t.color("white")
t.speed("fastest")
t.shape("square")
t.penup()
t.direction="stop"

f=Turtle()#먹이
f.speed("fastest")
f.shape("circle")
f.color("white")
f.penup()
f.goto(0,100)

arr=[]

#점수
p=Turtle()
p.speed("fastest")
p.color("white")
p.penup()
p.hideturtle()
p.goto(-470,320)
p.write("점수: 0 최고 점수: 0", font=("@Fixedsys", 20, "normal"))

#함수정의
def up():
    if t.direction != "down":
        t.direction = "up"

def down():
    if t.direction != "up":
        t.direction = "down"

def left():
    if t.direction != "right":
        t.direction = "left"

def right():
    if t.direction != "left":
        t.direction = "right"

def move():
    if t.direction == "up":
        y = t.ycor()
        t.sety(y + 20)

    if t.direction == "down":
        y = t.ycor()
        t.sety(y - 20)

    if t.direction == "left":
        x = t.xcor()
        t.setx(x - 20)

    if t.direction == "right":
        x = t.xcor()
        t.setx(x + 20)

#이동
win.listen()
win.onkeypress(up,"w")
win.onkeypress(down,"s")
win.onkeypress(right,"d")
win.onkeypress(left,"a")

while True:
    win.update()

    # 충돌 검사
    if t.xcor()>490 or t.xcor()<-490 or t.ycor()>340 or t.ycor()<-340:
        time.sleep(1)
        t.goto(0, 0)
        t.direction = "stop"
        for segment in arr:
            segment.goto(1000, 1000)
        arr.clear()
        s=0
        delay=0.1
        p.clear()
        p.write("점수: {}  최고 점수: {}".format(s, hs), font=("@Fixedsys", 20, "normal"))

    # 먹이먹기
    if t.distance(f) < 20:
        x = random.randint(-490, 490)
        y = random.randint(-240, 240)
        f.goto(x, y)

        # 꼬리 추가
        new_seg=Turtle()
        new_seg.speed("fastest")
        new_seg.shape("square")
        new_seg.color("grey")
        new_seg.penup()
        arr.append(new_seg)

        s += 10

        if s>hs:
            hs=s

        p.clear()
        p.write("점수: {}  최고 점수: {}".format(s, hs),font=("@Fixedsys", 20, "normal"))

        delay -= 0.001

    # 꼬리 움직임
    for i in range(len(arr) - 1, 0, -1):
        x = arr[i- 1].xcor()
        y = arr[i- 1].ycor()
        arr[i].goto(x, y)

    if len(arr) > 0:
        x = t.xcor()
        y = t.ycor()
        arr[0].goto(x, y)

    move()

    # 자살검사
    for segment in arr:
        if segment.distance(t) < 20:
            time.sleep(1)
            t.goto(0, 0)
            t.direction = "stop"
            for segment in arr:
                segment.goto(1000, 1000)
            arr.clear()
            s = 0
            delay = 0.1
            p.clear()
            p.write("점수: {}  최고 점수: {}".format(s, hs),font=("@Fixedsys", 20, "normal"))

    time.sleep(delay)

win.mainloop()
