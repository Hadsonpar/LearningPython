# 1. Data types built-in by default in Python:
    # text type         : str
    # number types      : int, float, complex
    # sequence types    : list, tuple, range
    # Mapping type      : dict
    # set type          : set, frozenset 
    # boolean type      : bool
    # binary type       : bytes, bytearray, memoryview
    # none type         : NoneType

# Assign a value according data types to the variables declared
xstr = "Hadson Paredes"
xint = 3
xflo = 3.11
xcom = 3j
xlit = ["benniger", 'intermediate', "advanced"]
xtup = ("benniger", 'intermediate', "advanced")
xran = range(3)
xdic = {"level": "benniger", 'cost': 150}
xset = {"benniger", 'intermediate', "advanced"}
xfro = frozenset({"benniger", 'intermediate', "advanced"})
xboo = True
xbyt = b"Hadson"
xbyt = bytearray(3)
xmom = memoryview(bytes(3))
xnon = None

# Note:
# Get the data type of any object by using the type() function:
print(type(xstr))