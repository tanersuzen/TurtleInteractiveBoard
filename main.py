import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("white")
drawing_board.title("Drawing Board")

turtle_instance = turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(100)

def angle_right():
    turtle_instance.right(10)

def angle_left():
    turtle_instance.left(10)

def clear_screen():
    turtle_instance.clear()

def return_home():
    turtle_instance.penup()
    turtle_instance.home()
    turtle_instance.pendown()

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward,key="space")
drawing_board.onkey(fun=angle_left,key="Up")
drawing_board.onkey(fun=angle_right,key="Down")
drawing_board.onkey(fun=clear_screen,key="c")
drawing_board.onkey(fun=return_home,key="h")

turtle.mainloop()