# Prints the statement below
print "I will now count my chickens:"

# Prints 'Hens' followed by the sum of 25 + 30 divided 6
print "Hens", float(25 + 30 / 6)

# Follows PEMDAS
# First Op is 25 * 3, returning 75
# Second Op is the 75 % 4, which is 3
#   This works by taking the largest largest number that 75
#   can be divided by evenly and not exceed 4, in this case 18
#   and yields the remainder which is 3.
#   25 * 3 = 75
#   75 % 4 (also called modulo) uses 18 as the largest number that can divide into 75 x4 times
#   This yields 3
# Third Op is then the int 100 - the int from modulo, 3,
#   Returns 97
print "Roosters", float(100 - 25 * 3 % 4)

# Prints a statement
print "Now I will count the eggs:"

# Following PEMDAS
# 4 modulo 2 = 0
# 3 + 2 + 1 - 5 + 0 - 1 / 4 + 6
# 3 + 2 + 1 - 5 + 0 - 0 + 6
# 6 - 5 + 6
# 1 + 6
# == 7
print float(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

# Prints a statement
print "Is it true that 3 + 2 < 5 - 7?"

# Checks if 3 + 2 is less then 5 - 7
print float(3 + 2 < 5 - 7)

# Prints 5
print "What is 3 + 2?", float(3 + 2)
# Prints -2
print "What is 5 - 7?", float(5 - 7)

# Prints a statement
print "Oh, that's why it's False."

# Prints a statement
print "How about some more."

# Checks the provided equation of 5 being greater than -2
print "Is it greater?", float(5 > -2)

# Check if 5 is greater than or equal to -2
print "Is it greater or equal?", float(5 >= -2)

# Checks if 5 is less than or equal to -2
print "Is it less or equal?", float(5 <= -2)

