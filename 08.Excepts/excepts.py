# Python Try Except
# Main consideration in Python for Try Except:
"""
- The "try" block lets you test a block of code for errors.
- The "except" block lets you handle the error.
- The "else" block lets you execute code when there is no error.
- The "finally" block lets you execute code, regardless of the result of the try- and except blocks.
"""
# 1. Exception Handling: Usually when an error occurs, or exception, 
#    Python will normally stop and generate an error message.

# =====================================================================
# Example 1 applying Exception Handling: The "try" block will generate
# an exception, because "name" variable is not defined.
try:
    print(name)
except:
    print("an exception occurred")
# =====================================================================


# 2. Many Exceptions:
    # We can define as many exception blocks, for example: if we want to 
    # execute a special block of code for a special kind of error:

# =====================================================================
    # Example 2.1 applying Exception NameError:

try:
    print(name)
except NameError:
    print("name variable is not defined")
except:
    print("an exception occurred, verify please")
# =====================================================================
    

# =====================================================================
    # Example 2.2 applying else:

try:
    print("Hadson")
except:
    print("an exception occurred, verify please")
else:
    print("execution, very well")
# =====================================================================


# =====================================================================
    # Example 2.3 applying finally:

try:
    print("Hadson")
except:
    print("an exception occurred, verify please")
finally:
    print("the program has completed correctly")
# =====================================================================