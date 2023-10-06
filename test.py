# All functions taken from "Python Numerical Methods", Kong, Siauw and Bayen 
# https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html
import pytest

def my_adder(a, b, c):
    """
    function to sum the 3 numbers
    Input: 3 numbers a, b, c
    Output: the sum of a, b, and c
    author:
    date:
    """
    
    # this is the summation
    out = a + b + c
    
    return out


def my_thermo_stat(temp, desired_temp):
    """
    Changes the status of the thermostat based on 
    temperature and desired temperature
    author
    date
    :type temp: Int
    :type desiredTemp: Int
    :rtype: String
    """
    if temp < desired_temp - 5:
        status = 'Heat'
    elif temp > desired_temp + 5:
        status = 'AC'
    else:
        status = 'off'
    return status
    
 
def have_digits(s):
    """
    Checks if a string has digits in it
    """
    
    out = 0
    
    # loop through the string
    for c in s:
        # check if the character is a digit
        if c.isdigit():
            out = 1
            break
            
    return out
    
 
def test_my_adder():
    assert my_adder(1, 2, 3) == 6


def test_my_thermo_stat():
    assert my_thermo_stat(10, 20) == 'Heat'
    assert my_thermo_stat(30, 20) == 'AC'
    assert my_thermo_stat(18, 20) == 'off'
    assert my_thermo_stat(22, 20) == 'off'

def test_have_digits():
    assert have_digits('test1') == 1
    assert have_digits('test') == 0

def area_of_rectangle(width, height):
    return width*height

def perimeter_of_rectangle(width,height):
    return (width+height)*2

@pytest.mark.parametrize("width,height,area", [(3, 5, 15), (2, 4, 8), (6, 9, 54)])
def test_area(width, height, area):
    output = area_of_rectangle(width, height)
    assert output == area

@pytest.mark.parametrize("width,height,perimeter", [(3, 5, 16), (2, 4, 12), (6, 9, 30)])
def test_perimeter(width, height, perimeter):
    output = perimeter_of_rectangle(width, height)
    assert output == perimeter
    

