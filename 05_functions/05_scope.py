def serve_chai():
    chai_type = "Masala" # local scope
    print(f"Inside function {chai_type}")
    
chai_type = "Lemon"
serve_chai()
print(f"Outside function: {chai_type}")

def chai_counter():
    chai_order = "lemon" #Enclosing scope
    def print_order():
        chai_order = "Ginger"
        print("Inner:", chai_order)
        print_order()
    print("Outer",chai_order)
    
chai_order = "Tulsi" #Global
chai_counter()
print("Global :",chai_order)

'''
Scope in Python
Scope refers to the region of a program where a variable can be accessed. 
It determines the visibility and lifetime of variables.
Python follows the LEGB rule to resolve variable names:

L – Local Scope
E – Enclosing Scope
G – Global Scope
B – Built-in Scope

Types of Scope in Python (LEGB Rule)

1.Local Scope (L)

Variables declared inside a function.
Accessible only within that function.
def demo():
    x = 10
    print(x)

2.Enclosing Scope (E)

Variables in an outer (enclosing) function.
Accessible by inner (nested) functions.
def outer():
    x = 20
    def inner():
        print(x)
    inner()

3.Global Scope (G)

Variables declared outside all functions.
Accessible throughout the program.
x = 30
def show():
    print(x)

4.Built-in Scope (B)

Predefined names provided by Python (e.g., print(), len(), max()).
print(len("Python"))

'''
