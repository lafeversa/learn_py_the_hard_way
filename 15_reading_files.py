# imports
from sys import argv

# setting the argument variables for the script, including script (seems to be similar
# to self) and the filename we specifiy and run of script
script, filename = argv

# opens the file we told it to - errors if no filename w/ the name exists
txt = open(filename)

# print
print "Here's your file %r:" % filename
# prints what is contained in the file
print txt.read()

# print
print "Type the filename again:"

# sets the var to raw_input
file_again = raw_input("> ")

# attempts to open a file with the name of the input above
txt_again = open(file_again)

# prints contents
print txt_again.read()

txt.close()
txt_again.close()