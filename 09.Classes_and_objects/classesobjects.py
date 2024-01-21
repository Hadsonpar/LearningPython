# Python classes and object normally is applying in Object Oriented
# Programming - (OOP), now we will review some exercises basic 
# class and objects

# Note:
# For define classes is use the class keyword, similar to how we define
# functions by using the def keyword.

# =====================================================================
# Example 1: A simple class with attributes
class animals:
    # attributes
    dog = "dog"
    cat = "cat"
    leo = "lion"
    tig = "tiger"
    jir = "giraffe"

# Now, we creating an object to instanced the class animals, the 
# instantiate will return us the attributes
animal = animals
print(animal.dog)
print(animal.cat)
print(animal.leo, animal.tig, animal.jir)
# =====================================================================

# =====================================================================
# Example 2: A class with attributes and method
class animals_type:
    # attributes
    dog = "dog"
    cat = "cat"
    leo = "lion"
    tig = "tiger"
    jir = "giraffe"

    # methods of class animals_type
    def domestic_types(self, types):
        print("Type "+types, self.dog, self.cat, sep=", ")
    
    def wild_types(self, types):
        print("Type "+types, self.leo, self.tig, self.jir, sep=", ")

# Now, we creating an object to instanced the class animals, the 
# instantiate will return us the methods
types = animals_type()
types.domestic_types("domestic")
types.wild_types("wild")
# =====================================================================