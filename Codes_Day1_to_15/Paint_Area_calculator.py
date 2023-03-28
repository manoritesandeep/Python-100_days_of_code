"""
You are painting a wall. 
The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. 
Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

number of cans = (wall height x wall width) ÷ coverage per can.

e.g. Height = 2, Width = 4, Coverage = 5

number of cans = (2 * 4) / 5

                           = 1.6

But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.
"""
import math

def paint_calc(wall_height: float, wall_width: float, coverage_per_can :int = 5):
    # coverage_per_can=5
    number_of_cans = (wall_height * wall_width) / coverage_per_can
    print(f"You'll need {math.ceil(number_of_cans)} cans of paint.")

paint_calc(3,9)