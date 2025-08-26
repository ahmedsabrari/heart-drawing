"""
Heart Drawing Animation using Python Turtle

This script creates a beautiful heart animation using parametric equations.
The mathematical functions generate a perfect heart shape with smooth animation.

Author: [Your Name]
Date: [Current Date]
Version: 1.0.0
"""

import math
from turtle import *

# Configuration constants - easily modifiable
BACKGROUND_COLOR = "black"
HEART_COLOR = "red"
PEN_SIZE = 2
DRAWING_SPEED = 0
SCALE_FACTOR = 20
TOTAL_POINTS = 6000
RETURN_TO_ORIGIN_FREQUENCY = 1  # Return to origin after each point

def heart_x(k):
    """
    Calculate the x-coordinate for the heart parametric equation.
    
    Args:
        k (float): Parameter for the parametric equation
        
    Returns:
        float: X-coordinate of the heart curve
    """
    return 15 * math.sin(k) ** 3

def heart_y(k):
    """
    Calculate the y-coordinate for the heart parametric equation.
    
    Args:
        k (float): Parameter for the parametric equation
        
    Returns:
        float: Y-coordinate of the heart curve
    """
    return (12 * math.cos(k) - 
            5 * math.cos(2 * k) - 
            2 * math.cos(3 * k) - 
            math.cos(4 * k))

def setup_drawing_environment():
    """Configure the turtle graphics environment."""
    speed(DRAWING_SPEED)
    bgcolor(BACKGROUND_COLOR)
    color(HEART_COLOR)
    pensize(PEN_SIZE)

def draw_heart():
    """Draw the heart shape using parametric equations."""
    for i in range(TOTAL_POINTS):
        # Calculate coordinates
        x = heart_x(i) * SCALE_FACTOR
        y = heart_y(i) * SCALE_FACTOR
        
        # Move to the calculated position
        goto(x, y)
        
        # Return to origin to create animation effect
        if i % RETURN_TO_ORIGIN_FREQUENCY == 0:
            goto(0, 0)

def main():
    """Main function to execute the heart drawing animation."""
    setup_drawing_environment()
    draw_heart()
    done()  # Keep the window open after drawing completes

if __name__ == "__main__":
    main()