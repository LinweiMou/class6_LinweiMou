## How To calculate the area of a rectangle?

You have a rectangle with its width and height already known.
If you want to get the area of this rectangle, you can do as following.

Download the code from this GitHub repository and place
the `example/` folder in the same directory as your
Python script:

    your_project/
    │
    ├── example/
    │   ├── __init__.py
    │   └── functions.py
    │
    └── your_script.py

Inside of `functions.py` you can now import the
`area_of_rectangle()` function from the `example.functions`
module:

    # your_script.py
    from example.functions import area_of_rectangle

After you've imported the function, you can use it
to calculate the area of a reactangle:

    # your_script.py
    from example.functions import area_of_rectangle

    print(area_of_rectangle(20, 10))  # OUTPUT: 400.0

You're now able to get the area of that rectangle, and you'll
always get a `float` as a result.

