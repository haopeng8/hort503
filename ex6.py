# types_of_people equals 10
types_of_people = 10
# x equals "there are (number defined in previous line) types of people"
x = f"There are {types_of_people} types of people."

# binary equals binary
binary = "binary"

# do_not equals don't
do_not = "don't"
# y equals "Those who know binary and those who don't", two variables defined previously
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
# {} is an empty variable defined by .format later (next line)
joke_evaluation = "Isn't that joke so funny?! {}"

# hilarious is a variable defined as False. .format put this variable to the empty {}
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# w and e can be printed together using "+"
print(w + e)
