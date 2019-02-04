# define the formatter string
formatter = "{} {} {} {}"

# put 1,2,3,4 to the formatter string
print(formatter.format(1, 2, 3, 4))

# put one, two, three, four to the formatter string
print(formatter.format("one", "two", "three", "four"))

# put True, False, False, True to the formatter string
print(formatter.format(True, False, False, True))

# put four formatter strings to the formatter string
print(formatter.format(formatter, formatter, formatter, formatter))

# Put the words to the formatter string in sequence
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
