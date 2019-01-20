>>> i = 100
>>> j = 4.0
>>> x = 30
>>> y = 90
>>>
>>> print("There are", i, "cars available")
There are 100 cars available
>>> print("There are only", j, "drivers available.")
There are only 4.0 drivers available.
>>> print("There are only", x, "drivers available.")
There are only 30 drivers available.
>>> print("There will be", i-x, "empty cars today.")
There will be 70 empty cars today.
>>> print("We can transport", x * j "people today.")
  File "<stdin>", line 1
    print("We can transport", x * j "people today.")
                                                  ^
SyntaxError: invalid syntax
>>> print("We can transport", x*j "people today.")
  File "<stdin>", line 1
    print("We can transport", x*j "people today.")
                                                ^
SyntaxError: invalid syntax
>>> print("We can transport", x*j, "people today.")
We can transport 120.0 people today.
>>> print("We have", y, "to carpool today.")
We have 90 to carpool today.
>>> print("We need to put about", y / x, "in each car.")
We need to put about 3.0 in each car.
>>> 
