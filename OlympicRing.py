import turtle

# A list that use for configure color
circle_color = ['blue','black','red','yellow','green']

orgin_cal = 300
# Coordinates
circle_pos = [
    
    [-1*orgin_cal,0],
    [0,0],
    [orgin_cal,0],
    [-0.5 * orgin_cal,-0.5 * orgin_cal],
    [0.5 * orgin_cal,-0.5 * orgin_cal]

    ]


def main():
    # Setting pen size
    turtle.pensize(orgin_cal/15)

    # start draw Olympic five rings
    for i in range(len(circle_color)):
        turtle.penup()
        turtle.goto(circle_pos[i][0],circle_pos[i][1])
        turtle.pendown()
        turtle.pencolor(circle_color[i])
        turtle.circle(orgin_cal/2-orgin_cal/10)
        i += 1



main()
turtle.mainloop()
