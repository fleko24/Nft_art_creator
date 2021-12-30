# import colorgram
# colors = colorgram.extract('example.jpg', 30)
# rgb_colors =[]
# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r,g,b)
#    rgb_colors.append(new_color)

# print(rgb_colors)
import random
import turtle

turtle.colormode(255)
tim = turtle.Turtle()
color_list = [(25, 108, 164), (194, 38, 81), (238, 161, 49), (234, 215, 85), (223, 137, 176), (144, 108, 56),
              (102, 197, 219), (206, 166, 29), (20, 57, 132), (214, 73, 90), (239, 89, 50), (141, 208, 227),
              (118, 192, 140), (3, 186, 176), (106, 107, 199), (138, 29, 73), (4, 161, 86), (98, 51, 36),
              (22, 156, 210), (232, 165, 184), (175, 185, 221), (29, 90, 95), (233, 172, 161), (152, 213, 190),
              (242, 205, 8), (89, 48, 31)]

# set initial position
tim.setheading(225)
tim.penup()
tim.hideturtle()
tim.speed("fastest")
tim.forward(300)
tim.setheading(0)

# loop
number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle.Screen()
screen.title("NFT dot art creator")
screen.exitonclick()
