import turtle
import random
from turtle import Screen
# import colorgram
# art=colorgram.extract('damien_hirst_spots_art.jpg',108) #change the value for num.of colors
# colours=[]
# for color in art:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     colours_in_image=(r,g,b)
#     colours.append(colours_in_image)
# print(colours)
'''USED TO EXTRACT COLOUR CODE FROM THE IMAGE'''

arrow=turtle.Turtle()
turtle.colormode(255)
arrow.shape("arrow")
#arrow.width(20)
arrow.speed(0)

art_colours=[(225, 154, 103), (125, 170, 199),(228, 71, 89), (222, 130, 151), (244, 210, 96), (20, 118, 155),
            (121, 180, 148), (33, 126, 89),(15, 169, 211), (224, 85, 77), (136, 89, 64), (175, 187, 221),
            (240, 149, 167), (112, 88, 101),(7, 173, 123), (245, 161, 143), (164, 211, 163), (0, 100, 123),
            (53, 58, 97), (159, 201, 216),(166, 150, 83), (19, 105, 74), (85, 129, 178), (244, 216, 11)]
            #WHITE COLOR IS REMOVED FROM THE LIST

# art_colours=[(252, 251, 251), (247, 249, 251), (225, 154, 103), (251, 244, 247), (249, 252, 250), (125, 170, 199),
#             (228, 71, 89), (222, 130, 151), (244, 210, 96), (20, 118, 155), (121, 180, 148), (33, 126, 89),
#             (15, 169, 211), (224, 85, 77), (136, 89, 64), (175, 187, 221), (240, 149, 167), (112, 88, 101),
#             (7, 173, 123), (245, 161, 143), (164, 211, 163), (0, 100, 123), (53, 58, 97), (159, 201, 216),
#             (166, 150, 83), (19, 105, 74), (85, 129, 178), (244, 216, 11)]
#             #ALL COLOURS FROM THE IMAGE


def up_move():
    up = 0
    for dot in range(9):
        arrow.penup()
        arrow.setx(0)
        arrow.sety(up)
        moving_dots()
        up+=60
    arrow.up()

def moving_dots():
    for dot in range(12):
        random_colour = random.choice(art_colours)
        arrow.dot(20,random_colour)
        arrow.penup()
        arrow.forward(50)
        arrow.pendown()
    arrow.penup()

up_move()
screen=Screen()
screen.exitonclick()

