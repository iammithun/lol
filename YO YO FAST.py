import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Yo-Yo Animation")

# Create the Yo-Yo turtle
yoyo = turtle.Turtle()
yoyo.shape("circle")
yoyo.color("red")
yoyo.penup()

# Yo-Yo initial position
yoyo.goto(0, 100)

# Create the string turtle
string = turtle.Turtle()
string.hideturtle()
string.penup()
string.goto(0, 200)
string.pendown()

# Function to animate the Yo-Yo
def animate_yoyo():
    for i in range(100, -101, -1):  # Move down
        yoyo.goto(0, i)
        string.clear()
        string.goto(0, 200)
        string.pendown()
        string.goto(0, i)
        screen.update()
    
    for i in range(-100, 101, 1):  # Move up
        yoyo.goto(0, i)
        string.clear()
        string.goto(0, 200)
        string.pendown()
        string.goto(0, i)
        screen.update()

# Set the screen to update continuously
screen.tracer(0)

# Animate the Yo-Yo indefinitely
while True:
    animate_yoyo()

# Close the turtle graphics window when clicked
screen.mainloop()
