import turtle as t
import random as r
import time
import math
import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(r"C:\Users\user\Music\Jingle Bell Rock (Instrumental Version).mp3")
pygame.mixer.music.play(-1)

class Firework:
    def __init__(self, x, y, particles, color_group):
        self.lifetime = r.randint(50, 70)  # 수명
        self.particles = []
        self.colors = color_group  # 색상 그룹 지정
        for _ in range(particles):
            angle = r.randint(0, 360)
            speed = r.uniform(2, 5)  # 초기 속도
            size = r.uniform(5, 10)  # 초기 크기
            self.particles.append({
                "angle": angle,
                "speed": speed,
                "x": x,
                "y": y,
                "size": size,
                "color": r.choice(self.colors),
                "alpha": 1.0  # 초기 투명도 (1: 불투명, 0: 투명)
            })
    def update(self):
        # 수명 감소
        self.lifetime -= 1
        # 각 입자 이동, 크기 감소 및 투명도 조정
        for p in self.particles:
            rad_angle = math.radians(p["angle"])  # 각도를 라디안으로 변환
            p["x"] += p["speed"] * math.cos(rad_angle)  # x 좌표 이동
            p["y"] += p["speed"] * math.sin(rad_angle)  # y 좌표 이동
            p["speed"] *= 0.95  # 속도 감소
            p["size"] *= 0.95  # 크기 감소
            p["alpha"] *= 0.9  # 투명도 감소

def draw_firework(t, firework):
    for p in firework.particles:
        if p["alpha"] > 0:  # 투명도가 남아있는 입자만 그림
            t.penup()
            t.goto(p["x"], p["y"])
            t.pendown()
            t.dot(int(p["size"]), p["color"])

# 트리 그리기
def draw_tree(t):
    t.penup()

    # 트리 모양을 그리기
    tree = [
        "        #        ",
        "       @@#       ",
        "      ####*      ",
        "     ##***##     ",
        "    #*#######    ",
        "      #@@@#      ",
        "    ######@@#    ",
        "  ##&&&&&&&####   ",
        " &&&&###########   ",
    ]
    stx = -110
    sty = 100
    for i, row in enumerate(tree):
        t.goto(stx, sty - i * 20)
        for j, char in enumerate(row):
            if char=='#': 
                t.color("green") #초록 #
                t.goto(stx + j * 10, sty - i * 20)
                t.begin_fill()
                t.circle(5)
                t.end_fill()
            if char=='*':
                t.color("blue") #파랑 *
                t.goto(stx + j * 10, sty - i * 20)
                t.begin_fill()
                t.circle(5) 
                t.end_fill()
            if char=='@':
                t.color("red") #빨강 @
                t.goto(stx + j * 10, sty - i * 20)
                t.begin_fill()
                t.circle(5)
                t.end_fill()
            if char=='&':
                t.color("yellow") #노랑 &
                t.goto(stx + j * 10, sty - i * 20)
                t.begin_fill()
                t.circle(5)
                t.end_fill()
    # 트리 줄기
    t.color("brown")
    trunk = [
        "      |   |       ",
        "      |___|       ",
    ]
    trky = -75
    for i, row in enumerate(trunk):
        t.goto(stx, trky - i * 20)
        t.write(row, align="left", font=("Courier", 12, "normal"))

def colur():
    colors = ["cyan", "deepskyblue", "white", "lightblue", "aliceblue"]
    return r.choice(colors)

# 메시지 그리기
def message():
    t.goto(-20, -120)
    t.color("white")
    t.write("Merry Christmas!", align="center", font=("@Fixedsys", 20, "normal"))

# 눈송이 생성
def create_snow():
    x = r.randint(-400, 400)
    y = r.randint(50, 200)
    return [x, y]

# 눈송이
def draw_snow(a, st):
    st.color("white")
    for i in a:
        st.goto(i[0], i[1])
        oneone(st)

def oneone(st):
    colur()
    st.pendown()
    st.setheading(r.randint(0, 360))  # 랜덤한 방향으로 회전
    st.color(colur())
    for i in range(6):  # 눈송이의 6개의 팔
        st.forward(5)
        st.backward(5)
        st.right(60)  # 60도씩 회전
    st.penup()

# 눈송이 이동
def move(snowflakes):
    for snowflake in snowflakes:
        rand = r.randint(5, 10)
        snowflake[1] -= rand
        if snowflake[1] < -200:
            snowflake[0] = r.randint(-400, 400)
            snowflake[1] = r.randint(50, 200)

def Star(s):
    s.penup()
    s.goto(-40, 126)
    s.pendown()
    s.color("yellow")
    s.begin_fill()
    for i in range(5):
        s.forward(20)
        s.right(144)  # 별 모양 그리기
    s.end_fill()

def mountain(pen):
    pen.penup()
    pen.goto(-400, -200)  # 시작 위치 설정
    pen.pendown()

    pen.fillcolor("darkgreen")
    pen.color("darkgreen")    
    pen.begin_fill()  # 채우기 시작

    for x in range(-400, 400, 10):
        y = -200 + abs(x) * 0.3 + r.randint(-10, 10)
        pen.goto(x, y)

    # 산 아래 부분 닫기
    pen.goto(400, -200)
    pen.end_fill()
    pen.begin_fill()
    pen.goto(-400, -200)
    pen.end_fill()

    pen.goto(-400, -199)
    
    pen.begin_fill()
    for i in range(2):
        pen.forward(800)
        pen.right(90)
        pen.forward(120)
        pen.left(270)
    pen.end_fill()

def mountain2(pen):
    pen.penup()
    pen.goto(-400, -200)  # 시작 위치 설정
    pen.pendown()

    pen.fillcolor("white")
    pen.color("white")    
    pen.begin_fill()  # 채우기 시작

    for x in range(-400, 400, 10):
        y = -200 + abs(x) * 0.4 + r.randint(-10, 10)
        pen.goto(x, y)

    # 산 아래 부분 닫기
    pen.goto(400, -200)
    pen.end_fill()
    pen.begin_fill()
    pen.goto(-400, -200)
    pen.end_fill()

    pen.goto(-400, -199)
    
    pen.begin_fill()
    for i in range(2):
        pen.forward(800)
        pen.right(90)
        pen.forward(120)
        pen.left(270)
    pen.end_fill()


def main():
    # 화면 설정
    screen = t.Screen()
    screen.bgcolor("black")
    screen.title("Christmas Tree")
    screen.tracer(0)
    t.hideturtle()

    # 트리 터틀과 눈송이 터틀 생성
    tr = t.Turtle()
    tr.hideturtle()
    tr.speed(0)

    st = t.Turtle()
    st.hideturtle()
    st.speed(0)

    pen = t.Turtle()
    pen.speed(0)
    pen.hideturtle()
    
    star = t.Turtle()
    star.hideturtle()
    star.speed(0)

    fireworks = []  # 불꽃놀이 리스트
    turtle = t.Turtle()
    turtle.hideturtle()
    turtle.speed(0)

    # 트리와 메시지 그리기
    draw_tree(tr)
    message()
    Star(star)
    mountain2(pen)
    mountain(pen)

    # 눈송이 초기화
    snowflakes = [create_snow() for _ in range(50)]

    # 메인
    while True:
        #눈송이만 이동
        move(snowflakes)
        st.clear()
        # 새로 눈송이 그리기
        draw_snow(snowflakes, st)

        if r.random() < 0.05:
            x = r.randint(-300, 300)
            y = r.randint(100, 300)
            particles = r.randint(20, 40)
            warm_colors = ["red", "orange", "green", "white"] 
            fireworks.append(Firework(x, y, particles, warm_colors))

        if r.random() < 0.05:
            x = r.randint(-300, 300)
            y = r.randint(100, 300)
            particles = r.randint(20, 40)
            cool_colors = ["blue", "purple", "white"]
            fireworks.append(Firework(x, y, particles, cool_colors))

        if r.random() < 0.05:
            x = r.randint(-300, 300)
            y = r.randint(100, 300)
            particles = r.randint(20, 40)
            green_red_colors = ["green", "red"]
            fireworks.append(Firework(x, y, particles, green_red_colors))

        # 화면 갱신
        turtle.clear()

        # 불꽃 업데이트
        for firework in fireworks:
            firework.update()
            draw_firework(turtle, firework)

        #불꽃 제거
        fireworks = [fw for fw in fireworks if fw.lifetime > 0]

        screen.update()  # 화면 업데이트
        time.sleep(0.03)

if __name__ == "__main__":
    main()
