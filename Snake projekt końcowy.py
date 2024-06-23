import turtle
import time
import random

delay = 0.1

# Screen
wn = turtle.Screen()
wn.title("Snake Game by Maciej Witkowski")
wn.bgcolor("white")
wn.setup(width=600, height=600)
wn.tracer(0)

# Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# Fruits
fruits = []
for _ in range(5):  # Creating 5 fruits
    fruit = turtle.Turtle()
    fruit.speed(0)
    fruit.shape("square")
    fruit.color("green")
    fruit.penup()
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    fruit.goto(x, y)
    fruits.append(fruit)

# Bombs
bombs = []
for _ in range(3):  # Creating 3 bombs
    bomb = turtle.Turtle()
    bomb.speed(0)
    bomb.shape("circle")
    bomb.color("black")
    bomb.penup()
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    bomb.goto(x, y)
    bombs.append(bomb)

# Score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))
score = 0
high_score = 0

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def reset_game():
    time.sleep(1)
    head.goto(0,0)
    head.direction = "stop"

    # Hide the segments
    for segment in segments:
        segment.goto(1000, 1000)

    # Clear the segments list
    segments.clear()

    # Reset the score
    global score, delay
    score = 0

    # Reset the delay
    delay = 0.1

    # Update the score display
    pen.clear()
    pen.write("Score: {}    High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

def add_segment():
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("grey")
    new_segment.penup()
    segments.append(new_segment)

# Keyboard binds
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main loop
while True:
    wn.update()

    # Collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        reset_game()

    # Check for collision with the food
    if head.distance(food) < 20: 
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment
        add_segment()

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}    High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Check for collision with fruits
    for fruit in fruits:
        if head.distance(fruit) < 20:
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            fruit.goto(x, y)

            # Add a segment
            add_segment()

            # Increase the score by 5
            score += 5

            if score > high_score:
                high_score = score

            pen.clear()
            pen.write("Score: {}    High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for collision with the body
    for segment in segments:
        if segment.distance(head) < 20:
            reset_game()

    # Check for collision with bombs
    for bomb in bombs:
        if head.distance(bomb) < 20:
            reset_game()

    time.sleep(delay)

wn.mainloop()
