# Importing the turtle module
import turtle

# Function to draw a heart shape
def draw_heart():
    turtle.fillcolor('red')  # Set the fill color to red
    turtle.begin_fill()      # Start filling the shape
    turtle.left(140)         # Turn left by 140 degrees
    turtle.forward(224)      # Move forward by 224 units
    turtle.circle(-112, 200) # Draw a circle with a negative radius
    turtle.left(120)         # Turn left by 120 degrees
    turtle.circle(-112, 200) # Draw another circle
    turtle.forward(224)      # Move forward by 224 units
    turtle.end_fill()        # End filling the shape

# Set up the turtle environment
turtle.speed(1)              # Set the speed of the turtle
draw_heart()                 # Call the function to draw the heart
turtle.done()                # Finish the drawing
