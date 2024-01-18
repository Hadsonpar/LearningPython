# Python has two primitive loop commands. Loops are used to repeat a block of code.
#   1. for loop
#   2. while loop
# ---------------------------------------------------------------------

# =====================================================================

# 1. Python For loop is used for sequential traversal i.e. it is used for
#    iterating over an iterable like String, Tuple, List, Set, or Dictionary. 

# For Loop Syntax
"""
for var in iterable:
    statements(var)
"""
# Example 1 - For loop: access items of a list using for loop
level = ["benniger", 'intermediate', "advanced"]
for items in level:
    print(items)

# Example 2 - For loop: use range() with a for loop to iterate a certain number of times
for i in range(4):
    print(i)

# Example 3 - For loop: loop through a string
x = "expert"
for expert in x:
    print(expert)
    
# Note: In Python, for loops only implement the collection-based iteration.
# =====================================================================

# =====================================================================
# 2. Python While Loop is used to execute a block of statements repeatedly 
#    until a given condition is satisfied.
    
# While Loop Syntax
"""
while expression:
    statement(s)
"""

# Example 1 While Loop: the condition for while will be True as 
# long as the counter variable (count) is less than 5. 
count = 0
while (count < 5): 
	count = count + 1
	print(count, "intermediate")

# Example 2 While Loop: infinite while Loop
age = 36
while age > 18: 
	print('infinite Loop')
      
# Example 3 While Loop: all letters except 'm' and 'a' 
i = 0
a = 'intermediate'

while i < len(a): 
	if a[i] == 'e' or a[i] == 's': 
		i += 1
		continue
		
	print('Capture of letters :', a[i]) 
	i += 1