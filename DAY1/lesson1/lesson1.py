from turtle import *

#we want to build house

#first DRAW square
width(7)
color("red")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)

left(90)
end_fill()
#END SQUARE DRAW
#NOW DRAW DOOR
forward(70)
color("BLACK")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
#END DOOR DRAW
#NOW DRAW ROOF
penup()
goto(200, 200)
pendown()

color("BLUE")
begin_fill()
right(150)
forward(200)
left(120) 
forward(200)
end_fill()
#END ROOF DRAW
#NOW DRAW WINDOWS
penup()
goto(50, 70)
pendown()
right(60)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
#FIRST WINDOW DONE
#SECOND WINDOW DRAW START
penup()
goto(150,70)
pendown()
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
#END SECOND WINDOW DRAW 
#NOW DRAW GRASS
penup()
goto(0,0)
pendown()
color("green")
begin_fill()
right(90)
forward(470)
left(90)
forward(390)
left(90)
forward(930)
left(90)
forward(390)
left(90)
forward(470)
end_fill()
forward(235)
#END DRAW GRASS
# NOW DRAW TREE
color("BROWN")
right(90)
forward(100)
color("DARK GREEN")
begin_fill()
left(90)
forward(20)
right(90)
forward(150)
right(90)
forward(40)
right(90)
forward(150)
right(90)
forward(20)
end_fill()
#END TREE DRAW 
#THE END
#ARTIST-TEMURI INAISHVILI





exitonclick()







