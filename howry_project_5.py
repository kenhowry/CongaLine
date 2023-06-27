"""
Conga Line - This program makes a line of circles that follow the mouse where it is dragged.
When the 'N' key is pressed, a new circle is created

File Name: howry_project_5.py
Author: Ken Howry
Date: 10.2.23
Course: COMP 1352
Assignment: Project V
Collaborators: N/A
Internet Source: N/A
"""

#imports
from random import random
import dudraw
from dudraw import Color

#class
class Dancer:
    def __init__(self, x_pos:float, y_pos:float, x_trgt:float, y_trgt:float, r = 0.01):
        """
        Description of Function: Sets variables
        Parameters: x_pos: float, x_position of circle 
        y_pos: float, x_position of circle  
        x_target: float, x_position of target 
        y_target: float, y_position of target 
        r: float, radius of circle
        Return: None
        """
        self.x_position = x_pos
        self.y_position = y_pos
        self.x_target = x_trgt
        self.y_target = y_trgt
        self.radius = r
        #assigning a random color
        self.color = Color(int(256*random()), int(256*random()), int(256*random()))

    def __str__(self):
        """
        Description of Function: String function for debugging
        Parameters: None
        Return: str
        """
        return f'{self.x_position}, {self.y_position}, {self.x_target}, {self.y_target}'
    def move(self):
        """
        Description of Function: Movement function
        Parameters: None
        Return: None
        """
        self.x_position += (self.x_target - self.x_position)*0.15
        self.y_position += (self.y_target - self.y_position)*0.15
    def set_target(self, x, y):
        """
        Description of Function: Sets target
        Parameters: None
        Return: None
        """
        self.x_target = x
        self.y_target = y
    def draw(self):
        """
        Description of Function: Draws the circle
        Parameters: None
        Return: None
        """
        dudraw.set_pen_color(self.color)
        dudraw.filled_circle(self.x_position, self.y_position, self.radius)
        dudraw.set_pen_color(dudraw.BLACK)
        dudraw.circle(self.x_position, self.y_position, self.radius)
    def random_color(self):
        self.color = Color(int(256*random()), int(256*random()), int(256*random()))
dancer_list = []
#making a list of dancers
for i in range(10):
    if i == 0:
        #line leader
        dancer_list.append(Dancer(random(), random(), dudraw.mouse_x(), dudraw.mouse_y()))
    else:
        dancer_list.append(Dancer(random(), random(), dancer_list[i-1].x_position, dancer_list[i-1].y_position))

key = ''

#while loop
while key != 'q':
    #moving dancers to their new position
    for dancer in dancer_list:
        dancer.move()
    #sets target of dancer equal to the mouse or cicle in front of it
    for i in range(len(dancer_list)):
        if i == 0:
            dancer_list[i].set_target(dudraw.mouse_x(), dudraw.mouse_y())
        else:
            dancer_list[i].set_target(dancer_list[i-1].x_position, dancer_list[i-1].y_position)
    #clearing and redrawing dancers
    dudraw.clear_rgb(217,179,255)
    for dancer in dancer_list:
        dancer.draw()
    #next_key_typed
    if dudraw.has_next_key_typed():
        key = dudraw.next_key_typed()
    #adding a dancer when 'n' is pressed
    if key == 'n':
        dancer_list.append(Dancer(random(), random(), dancer_list[-1].x_position, dancer_list[-1].y_position))
        key = ''
    dudraw.show(50)