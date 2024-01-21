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

# text type         : str
# ---------------------------------------------------------------
xstr = "Hadson Paredes"
print(xstr)
# ---------------------------------------------------------------

# number types      : int, float, complex
# ---------------------------------------------------------------
xint = 3
xflo = 3.11
xcom = 3j
print(xint, xflo, xcom)
# ---------------------------------------------------------------

# sequence types    : list, tuple, range
# ---------------------------------------------------------------
xlit = ["beginner", 'intermediate', "advanced"]
xtup = ("beginner", 'intermediate', "advanced")
xran = range(3)
print(xlit, xtup, xran)
# ---------------------------------------------------------------

# Mapping type      : dict
# ---------------------------------------------------------------
xdic = {"level": "beginner", 'cost': 150}
print(xdic)
# ---------------------------------------------------------------

# set type          : set, frozenset 
# ---------------------------------------------------------------
xset = {"beginner", 'intermediate', "advanced"}
xfro = frozenset({"beginner", 'intermediate', "advanced"})
print(xset, xfro)
# ---------------------------------------------------------------

# boolean type      : bool
# ---------------------------------------------------------------
xboo = True
print(xboo)
# ---------------------------------------------------------------

# binary type       : bytes, bytearray, memoryview
# ---------------------------------------------------------------
xbyt = b"Hadson"
xbya = bytearray(3)
xmom = memoryview(bytes(3))
print(xbyt, xbya, xmom)
# ---------------------------------------------------------------

# none type         : NoneType
# ---------------------------------------------------------------
xnon = None
print(xnon)
# ---------------------------------------------------------------

# Note:
# Get the data type of any object by using the type() function:
print(type(xstr))