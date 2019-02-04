# define the function of cheese_and_crackers. It has two variables
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
# assign values to the two variables in the cheese_and_crackers function
cheese_and_crackers(20, 30)

# assign values to two new global variables
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# assign the two variables to the cheese_and_crackers function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Do add work for the two variables
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# same as above, but add number to the variable value
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
