# How many cars we have
cars = 100

# How many passengers can be put in each car
space_in_a_car = 4.0

# How many drivers we have
drivers = 30

# How many passengers we need to transport
passengers = 90

# No-driven cars equals cars available substracted by drivers available
cars_not_driven = cars - drivers

# Driven cars equals drivers available
cars_driven = drivers

# Carpool capacity equals driven cars multiplied by passenger spots in each car
carpool_capacity = cars_driven * space_in_a_car

# Average passengers in each car equals the amount of all passsenges divided by the amount of cars being driven
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("Thre will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
