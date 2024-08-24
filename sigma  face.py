import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create the turtle
face = turtle.Turtle()
face.speed(3)

def draw_circle(color, radius, x, y):
    face.penup()
    face.color(color)
    face.fillcolor(color)
    face.goto(x, y)
    face.pendown()
    face.begin_fill()
    face.circle(radius)
    face.end_fill()

def draw_sigma(x, y):
    face.penup()
    face.goto(x, y)
    face.pendown()
    face.write("Σ", font=("Arial", 40, "normal"))

# Draw the face
draw_circle("yellow", 100, 0, -100)

# Draw the eyes
draw_circle("black", 15, -35, 35)
draw_circle("black", 15, 35, 35)

# Draw the sigma mouth
draw_sigma(-15, -40)

# Hide the turtle
face.hideturtle()

# Keep the window open until clicked
screen.mainloop()
