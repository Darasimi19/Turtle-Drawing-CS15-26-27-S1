from turtle import*

size = 80
#base
color("red")
forward(size)
left(90)
forward(size)
left(90)
forward(size)
left(90)
forward(size)
left(90)

#roof
left(90)
forward(size)

#connecting the roof
color("orange")
right(30)
forward(size)
right(120)
forward(size)

#door prep
penup()
right(30)
forward(size)
right(90)
forward(size * 0.3)
right(90)

#the actual door
pendown()
color("blue")
forward(size * 0.4)
left(90)
forward(size * 0.3)
left(90)
forward(size * 0.4)

done()
