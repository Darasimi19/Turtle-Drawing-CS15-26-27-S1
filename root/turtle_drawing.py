from turtle import*

size = 80
door_height = 35
door_width = 20
ray_length = 20
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
forward(28)
right(90)

#the actual door
pendown()
color("blue")
forward(door_height)
left(90)
forward(door_width)
left(90)
forward(door_width)
forward(15)

#star
penup()
left(90)
forward(60)
left(90)
forward(120)
color("yellow")

#  drawing the star
pendown()
forward(ray_length)
backward(ray_length)
left(45)
forward(ray_length)
backward(ray_length)
left(45)
forward(ray_length)
backward(ray_length)
left(45)
forward(ray_length)
backward(ray_length)
left(45)
forward(ray_length)
backward(ray_length)
left(45)
forward(ray_length)
backward(ray_length)
left(45)
forward(ray_length)
backward(ray_length)
left(45)
forward(ray_length)
backward(ray_length)

done()
