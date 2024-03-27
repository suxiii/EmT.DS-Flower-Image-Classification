import turtle 

# create flower with 3 petals using turtle graphics

def draw_petal():
    turtle.width(5)  # Set line thickness to 5
    for _ in range(2):
        turtle.forward(100)
        turtle.right(60)
        turtle.forward(100)
        turtle.right(120)

def draw_flower():
    turtle.color('pink')
    turtle.bgcolor('black')
    turtle.goto(0, 0)
    turtle.pendown()
    for _ in range(3):
        draw_petal()
        turtle.right(120)
    turtle.done()
draw_flower()



