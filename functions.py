"""several functions come from the CMSE890-402 class.

This module is just some examples.

The module contains the following functions:

- `my_adder(a, b, c)` - Returns the sum of 3 numbers.
- `my_thermo_stat(temp, desired_temp)` - Returns the status of the thermostat.
- `have_digits(s)` - Returns any digits in the input string.
- `area_of_rectangle(width, height)` - Returns the area of rectangle.
- `perimeter_of_rectangle(width, height)` - Returns the perimeter of rectangle.
"""

from typing import Union

def my_adder(a: float, b: float, c: float) -> float:
    """Function to sum 3 numbers
    
    input 3 numbers you have, then the function will calculate the sum of the 3 numbers and output it

    Arg:
        a: first input number with the type of float

        b: second input number with the type of float

        c: third input number with the type of float 

    Returns:
        out: the sum of the input 3 numbers with the type of float
    """
    # this is the summation
    out = a + b + c
    
    return out

def my_thermo_stat(temp: float, desired_temp: float) -> str:
    """Changes the status of the thermostat
    
    Changes the status of the thermostat based on temperature and desired temperature

    Arg:
        temp: the temperature for now with the type of float

        desired_temp: the temperature you want with the type of float

    Returns:
        status: three type of status for now, Heat (need to heat up), AC (need to cool down) and off (turn off), with type of str
    """
    if temp < desired_temp - 5:
        status = 'Heat'
    elif temp > desired_temp + 5:
        status = 'AC'
    else:
        status = 'off'
    return status
    
 
def have_digits(s: str) -> int:
    """Checks if a string has digits in it
    
    if there is any digits in the input string, this function will judge it

    Arg:
        s: the input string with the type of str

    Returns:
        out: type of int, it should be 1 (there is digit or are digits in the input string) or 0 (no digit in the input string). 
    """
    
    out = 0
    
    # loop through the string
    for c in s:
        # check if the character is a digit
        if c.isdigit():
            out = 1
            break
            
    return out
    
def area_of_rectangle(width: float, height: float) -> float:
    """calculate the area of a rectangle
    
    input the width and height of a rectangle, by this function, you can get the area of it

    Arg:
        width: the width of rectangle with the type of float

        height: the heigth of rectangle with the type of float

    Returns:
        area: area of the rectangle with the type of float. 
    """    
    area = width*height
    return area

def perimeter_of_rectangle(width: float, height: float) -> float:
    """calculate the perimeter of a rectangle
    
    input the width and height of a rectangle, by this function, you can get the perimeter of it

    Arg:
        width: the width of rectangle with the type of float

        height: the heigth of rectangle with the type of float

    Returns:
        perimeter: perimeter of the rectangle with the type of float. 
    """     
    perimeter = (width+height)*2
    return perimeter
