from sys import argv

script, input_file = argv

# define the print_all function, print what have been read from input_file
def print_all(f):
    print(f.read())

# define the rewind function, which move to the start of the file
def rewind(f):
    f.seek(0)

# define the function print_a_line
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

# print_all means print the read as defined in line 7
# current_file is the read target
# current_file means open the input_file
print_all(current_file)

print("Now let's rewind, kind of like a tape")

# in line 10 and 11, the function rewind is defines as go back to the beginning of the file
# current_file is the opened input_file, so go back to beginning of the input_file
rewind(current_file)

print("let's print three lines:")

# defined in line 14 and 15. print 1 and the first line by the readline function
current_line = 1
print_a_line(current_line, current_file)

# print 2 and second line. readline function stop at the first line last time, now begin the second line
current_line = current_line + 1
print_a_line(current_line, current_file)

# the readline function begin read the third line. print by the print_a_line function
current_line = current_line + 1
print_a_line(current_line, current_file)
