import turtle  as t
import random
import time

screen = t.Screen()
screen.setup(height=500, width=600)
guess = screen.textinput(prompt="Dự đoán con rùa nào chiến thắng?", title="Nhập vào màu rùa (đỏ, nâu, xanh dương, xanh lá cây, cam, hồng)")
colors = ["red", "brown", "blue", "green", "orange", "pink"]
y_position = [0, -30, 30, -60, 60, 90]
turtle_speed = [10, 15, 20, 25, 30, 5]

# Tạo một list để lưu các con rùa
all_turtles = []
run = True

for turtle in range(0, 6):
    turtles = t.Turtle(shape="turtle")
    turtles.penup()
    # Di chuyển rùa về vị trí ban đầu,
    # bên trái cùng của đường đua
    turtles.goto(x=-250, y=y_position[turtle])
    # Màu của rùa
    turtles.color(colors[turtle])
    # Lưu vào list
    all_turtles.append(turtles)
start=time.time()
def random_walk(turtles):
    global run
    global color
    for turtle in turtles:
        turtle.forward(random.choice(turtle_speed))
        # Kiểm tra điều kiện cán đích
        # Khi 1 con cán đích thì dừng lại
        if turtle.xcor() > 250:
            run = False
            v,m =turtle.color()
            print("rua thang cuoc:",v)
            stop=time.time()
            print("thoi gian rua thang cuoc chay la: ",stop-start)
            break
while run:
    random_walk(all_turtles)

screen.exitonclick()
