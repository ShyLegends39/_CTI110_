# Brief Description: This program work on drawing my first and last initials for to be display turtle!
# I did tried to get them not to over lap each other, but came up with an idea of putting my last initial first and
# then my first initial. You will see what I mean when you run this one!? (I also got little fancy with this one, too?!)

# CTI-110

# P4LAB1b - Initials

# Kelly Bullard

# November 3, 2022

#

import turtle          
win = turtle.Screen()

# Added some display options to make this special for my last initial
tb = turtle.Turtle()    # The tb = is for last initials
tb.pensize(10)            # For pen's size
tb.pencolor("gray")     # Pen's color 
tb.shape("turtle")          # For pen's icon shape
tb.fillcolor('red')     # This fill is here for when this turtle starts
tb.penup()
# Drawing a straight line for tb
tb.goto(30,50) # Screen alignment
tb.pendown()

tb.right(90)
tb.forward(200)
 
tb.penup()
tb.goto(30,50) # Screen alignment
# Drawing the first curve for tb
tb.pendown()
tb.right(-90)
tb.circle(-50,180)
 
 
tb.penup()
tb.goto(30,-50) # Screen alignment
# The second curve for tb
tb.pendown()
tb.right(180)
tb.circle(-50,180)
tb.fillcolor('green') # This fill is here for when this turtle stops

t = turtle.Turtle()    # The t = is for first initials
# Added some display options to make this special for my first initial
t.pensize(10)            # Pen's size 
t.pencolor("pink")     # Pen's color 
t.shape("turtle")       # The pen's icon shape
t.fillcolor('skyblue') # This fill is here for when this turtle starts
t.penup()
# Drawing a straight line for t
t.goto(-30,50) # Screen alignment
t.pendown()
# Next for t
t.right(90)
t.forward(150)
# Then for t 
t.goto(-30,-20) # Screen alignment
t.left(45)
t.forward(100)
# Lastly for t 
t.goto(-30,-20) # Screen alignment
t.left(90)
t.forward(100)


t.fillcolor('green') # This fill is here for when this turtle stops
# End commands
win.mainloop()      # Waits for the user to close window
