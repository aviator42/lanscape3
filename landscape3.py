import turtle

scn = turtle.Screen()
scn.bgcolor("light blue")


jim = turtle.Turtle()
dwight = turtle.Turtle()
mike =  turtle.Turtle()

jim.penup()
jim.goto(0, 0)
jim.pendown()

jim.fillcolor("green")
jim.begin_fill()

jim.forward(700)
jim.right(90)
jim.forward(500)
jim.right(90)
jim.forward(1400)
jim.right(90)
jim.forward(500)
jim.right(90)
jim.forward(700)
jim.end_fill()



turtle.exitonclick()