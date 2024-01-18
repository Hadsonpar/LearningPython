# TYPES OF PYTHON OPERATORS
# 1. Python Arithmetic Operators
# 2. Python Comparison Operators
# 3. Python Logical Operators
# 4. Python Identity Operators
# 5. Python Bitwise Operators
# 6. Python Assignment Operators
# 7. Python Membership  Operators
# ---------------------------------------------------------------------

# =====================================================================
# 1. Python Arithmetic Operators
# OPERATOR	OPERATION	    DESCRIPTION
#   +	    Addition	    Adds two operands
#   -	    Subtraction	    Subtracts two operands
#   *	    Multiplication	Multiplies two operands
#   /	    Division	    Divides the first operand by the second
#   //	    Floor Division	Divides the first operand by the second
#   %	    Modulo	        Returns the remainder when the first operand is divided by the second
#   **	    Power	        Returns first raised to power second

# Example in Python Arithmetic Operators 
print("Addition", 8 + 2)
print("Subtraction", 7 - 2)
print("Multiplication", 6 * 4)
print("Division", 3 / 2)
print("Floor Division",	10 // 3)
print("Modulo", 5 % 2)
print("Power", 4 ** 2)
# =====================================================================

# =====================================================================
# 2. Python Comparison Operators
# OPERATOR	NAME
#   ==	    Equal
#   !=	    Not equal
#   >	    Greater than
#   <	    Less than
#   >=	    Greater than or equal to
#   <=	    Less than or equal to

# Example in Python Comparison Operators
print("Equal", 8 == 2)
print("Not equal", 7 != 2)
print("Greater than", 6 > 4)
print("Less than", 3 < 2)
print("Greater than or equal to",	10 >= 3)
print("Less than or equal to", 5 <= 2)
# =====================================================================

# =====================================================================
# 3. Python Logical Operators
# OPERATOR	DESCRIPTION
#   and 	Returns True if both statements are true
#   or	    Returns True if one of the statements is true
#   not	    Reverse the result, returns False if the result is true

# Example in Python Logical Operators
x = 3
print(x < 5 and  x < 10)
print(x < 5 or x < 4)
print(not(x < 5 and x < 10))
# =====================================================================

# =====================================================================
# 4. Python Identity Operators
# OPERATOR	DESCRIPTION
#   is 	    Returns True if both variables are the same object
#   is not	Returns True if both variables are not the same object

# Example in Python Identity Operators
x = 30
y = 36
z = x

print(x is not y)   # True
print(x is z)       # True

print(x is not z)   # False
print(z is y)       # False
# =====================================================================

# =====================================================================
# 5. Python Bitwise Operators
# OPERATOR	DESCRIPTION
#   &	    Bitwise AND
#   |	    Bitwise OR
#   ~	    Bitwise NOT
#   ^	    Bitwise XOR
#   >>	    Bitwise right shift
#   <<	    Bitwise left shift

# Example in Python Bitwise Operators
a = 10
b = 5
print(a & b)    # AND 
print(a | b)    # OR 
print(~a)       # NOT
print(a ^ b)    # XOR
print(a >> 3)   # right shift
print(a << 3)   # left shift
# =====================================================================

# =====================================================================
# 6. Python Assignment Operators
# OPERATOR	DESCRIPTION
#   =	    Assignment Operator
#   +=	    Addition Assignment
#   -=	    Subtraction Assignment
#   *=	    Multiplication Assignment
#   /=	    Division Assignment
#   %=	    Remainder Assignment
#   **=	    Exponent Assignment
#   //=	    Floor Division Assignment

# Example in Python Assignment Operators
a = 5
print("Assignment: ", a)

a += 5
print ("Addition: ", a)

a -= 5
print ("Subtraction: ", a)

a *= 5
print ("Multiplication: ", a)

a /= 5
print ("Division: ",a)

a %= 3
print ("Remainder: ", a)

a **= 2
print ("Exponent: ", a)

a //= 3
print ("Floor Division: ", a)
# =====================================================================

# =====================================================================
# 7. Python Membership  Operators
# OPERATOR	DESCRIPTION
#   in 	    Returns True if a sequence with the specified value is present in the object	
#   not in	Returns True if a sequence with the specified value is not present in the object

# Example in Python Membership Operators
x = ["benniger", 'intermediate', "advanced"]
print("intermediate" in x)  # in
print("expert" not in x)    # not in
# =====================================================================