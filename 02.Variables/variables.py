# Python tutorial - Variables

# ---------------------------------------------------------------
# DEFINITION OF VARIABLES - TOPICS:
# 1. Creating variables and assign values main
# 2. Assign Multiple Values
# 3. Global Variables
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# ---------------------------------------------------------------
# 1. Creating variables and assign values main
x = 'Hello'
y = "Hadson"
z = 36

print(x, y, z)

# 1.1. Assigning new value to "x" variable
x = "Welcom"
print(x, y, z)

# 1.2. Assigning new value to "z" variable of type string
z = "Paredes"
print(x, y, z)
print(x, y +" "+z, sep=", ")
print(type(x), type(y), type(z)) # finally all variables the are string type


# ---------------------------------------------------------------
# ---------------------------------------------------------------
# 2. Assign Multiple Values
# 2.1. Assign values to multiple variables in one line
level_benniger, level_intermediate, level_advanced, program_language = "benniger", 'intermediate', "advanced", 'Python 3'
print(level_benniger)
print(level_intermediate)
print(level_advanced)
print(program_language)

# 2.2. To list (collection) the values multiple in one value
levels = level_benniger, level_intermediate, level_advanced, program_language
print(levels)

# 2.3. Unpack a Collection, extract the values into variables
x, y, z, x1 = levels
print(x)
print(y)
print(z)
print(x1)
print(x, y, z, x1)


# ---------------------------------------------------------------
# ---------------------------------------------------------------
# 3. Global Variables
# 3.1. Creating blobal variable and assign values main
xglobal = "Tutorials for"
print(xglobal, level_benniger)

# 3.2. Complete the phrase, with a string, the global variable and an value of collection
print("Learning Python - ", xglobal, level_intermediate)

# Remember:
# The print() function prints the specified message to the screen, or other
# standard output device. In all topics applying the print() function for 
# view our result.