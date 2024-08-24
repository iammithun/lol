import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("lightblue")

# Create a turtle object
teddy = turtle.Turtle()
teddy.speed(5)

# Draw the teddy bear
def draw_circle(color, radius, x, y):
    teddy.penup()
    teddy.fillcolor(color)
    teddy.goto(x, y)
    teddy.pendown()
    teddy.begin_fill()
    teddy.circle(radius)
    teddy.end_fill()

def draw_rectangle(color, width, height, x, y):
    teddy.penup()
    teddy.fillcolor(color)
    teddy.goto(x, y)
    teddy.pendown()
    teddy.begin_fill()
    for _ in range(2):
        teddy.forward(width)
        teddy.right(90)
        teddy.forward(height)
        teddy.right(90)
    teddy.end_fill()

def draw_heart(color, x, y, size):
    teddy.penup()
    teddy.fillcolor(color)
    teddy.goto(x, y)
    teddy.pendown()
    teddy.begin_fill()
    teddy.left(140)
    teddy.forward(size)
    for _ in range(200):
        teddy.right(1)
        teddy.forward(2)
    teddy.left(120)
    for _ in range(200):
        teddy.right(1)
        teddy.forward(2)
    teddy.forward(size)
    teddy.end_fill()

# Draw the head
draw_circle("chocolate", 50, 0, 0)

# Draw the ears
draw_circle("chocolate", 20, -40, 60)
draw_circle("chocolate", 20, 40, 60)

# Draw the eyes
draw_circle("white", 8, -20, 10)
draw_circle("white", 8, 20, 10)
draw_circle("black", 4, -20, 10)
draw_circle("black", 4, 20, 10)

# Draw the nose
draw_circle("red", 5, 0, -10)

# Draw the mouth
teddy.penup()
teddy.goto(-15, -20)
teddy.pendown()
teddy.setheading(-60)
teddy.circle(15, 120)
teddy.hideturtle()

# Draw the body
draw_rectangle("chocolate", 80, 100, -40, -110)

# Draw the arms
draw_rectangle("chocolate", 30, 90, -70, -40)
draw_rectangle("chocolate", 30, 90, 40, -40)

# Draw the legs
draw_rectangle("chocolate", 20, 80, -25, -200)
draw_rectangle("chocolate", 20, 80, 5, -200)

# Draw the feet
draw_circle("chocolate", 25, -25, -240)
draw_circle("chocolate", 25, 15, -240)

# Draw the heart
draw_heart("red", 0, -130, 20)

# Hide the turtle and display the result
teddy.hideturtle()
screen.mainloop()
