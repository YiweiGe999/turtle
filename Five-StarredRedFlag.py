from turtle import *
from math import *
from time import *

# Star angle configuration, unit: degree
star_angle = [18,90,162,234,306,18]

# Star angle offset, unit: degree
angle_off = [0, 30.9, 8.1, -8.1,-30.9]

# Draw five star sequence
draw_seq = [0,2,4,1,3,0]


# Set star radius size
def set_rad_size(flag_len):


    rad_list = []
    rad_list.append(flag_len/10)
    rad_list.append(flag_len/30)
    rad_list.append(flag_len/30)
    rad_list.append(flag_len/30)
    rad_list.append(flag_len/30)
    
    return rad_list;


# Set star position x asix offset
def set_x_offset(length):

    offset_x_list = []
    offset_x_list.append(-1 *  length/2 +  length / 6)
    offset_x_list.append(-1 *  length/2 +  length * 0.3) 
    offset_x_list.append(-1 *  length/2 +  length * 0.4) 
    offset_x_list.append(-1 *  length/2 +  length * 0.4)
    offset_x_list.append(-1 *  length/2 +  length * 0.3)

    return offset_x_list;

# Set star position y asix offset
def set_y_offset(hight):

    offset_y_list = []
    offset_y_list.append(hight * 0.25)
    offset_y_list.append(hight * 0.4) 
    offset_y_list.append(hight * 0.3) 
    offset_y_list.append(hight * 0.15) 
    offset_y_list.append(hight * 0.05)
    
    return offset_y_list;


# Star draw star
def draw_star(rad_size,offset_x_val,offset_y_val,angle_offset):
    penup()
    # Set pen color to yellow
    color("yellow")
    begin_fill()
    
    
    for i in range(len(star_angle)):
        # Calculate the radians of the five angles relative to the center  
        radian = (star_angle[draw_seq[i]] +  angle_offset) / 180 * pi
        x = rad_size * cos(radian)
        y = rad_size * sin(radian)

        # Move to position (x,y)
        setpos(x+ offset_x_val,y+ offset_y_val)
    pendown()

    end_fill()
    
# Draw red flag
def draw_flag(length,hight):

    penup()
    setpos(-1 * length/2,-1 * hight/2)
    pendown()
    color("red")
    begin_fill()

    fd(length)
    left(90)
    fd(hight)
    left(90)
    fd(length)
    left(90)
    fd(hight)
    end_fill()




def main():

    
    FLAG_LENTH = 900
    FLAG_HIGHT  = FLAG_LENTH * 2 /3

    flag_length = FLAG_LENTH
    flag_hight = FLAG_HIGHT
    
    for len_index in range(1):
        reset()
        rad = set_rad_size(flag_length)

        offset_x = set_x_offset(flag_length)

        offset_y = set_y_offset(flag_hight)
        # Start draw red flag
        draw_flag(flag_length,flag_hight)

        # Start draw five stars
        for index in range(5):
            draw_star(rad[index],offset_x[index],offset_y[index],angle_off[index])
        
        color("red")
        penup()
        sleep(1)
        flag_length = FLAG_LENTH *  (len_index + 1)
        flag_hight = FLAG_HIGHT * (len_index + 1)
         
main()
mainloop()

