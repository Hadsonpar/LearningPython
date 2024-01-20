# Creating a Function in Python is defined using the def keyword:

# 1. Example
def function_name():
    print('hello!')

# calling the Function: function_name()
function_name()
# =====================================================================

# =====================================================================
# In python can be passed into the function arguments for 
# return a value, is necessary use the return statement.
# Example 2:  Creating a function name "days" with parameter "code"
def days(code):
    if (code == 1):
        day = "Sunday"
    if (code == 2):
        day = "Monday"
    if (code == 3):
        day = "Tuesday"
    if (code == 4):
        day = "Wednesday"
    if (code == 5):
        day = "Thursday"
    if (code == 6):
        day = "Friday"
    if (code == 7):
        day = "Saturday"
    return day

# Calling the Function days(1) passing function the argument 1
print(days(1))
# =====================================================================

# =====================================================================
# Example 3: Use default parameter value
def aussie_greeting(arg='Python!'):
    print(arg)
 
aussie_greeting()           # Uses default value
aussie_greeting("Hello")    # Change default parameter value
# =====================================================================

# =====================================================================
# Example 4: Creating a function name "addition" with 2 parameters "val1 and val2"
def addition(val1, val2):
    return val1 + val2

add = addition(8, 2)
print(add)
# =====================================================================