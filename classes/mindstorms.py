import turtle


def draw_square(turtle):

    for i in range(1,5):
        turtle.forward(100)
        turtle.right(90)
    

def draw_art():
    window = turtle.Screen()
    window.bgcolor('red')
    
    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('yellow')
    brad.speed(2)
    draw_square(brad)
    window.exitonclick() 

draw_art()    