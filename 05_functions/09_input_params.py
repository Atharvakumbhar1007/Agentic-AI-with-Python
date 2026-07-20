# chai = "Ginger chai"

# def prepare_chai(order):
#     print("preparing ", order)
    
# prepare_chai(chai)
# print(chai)

chai = [1, 2, 3]

def edit_chai(cup): #'cup' is parameter
    cup[1] = 421
    
edit_chai(chai) # 'chai' is argument
print(chai)

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)
    
make_chai("Darjeeling", "yes","low") #positional
make_chai(tea="Green", sugar="Medium",milk="No") #keywords