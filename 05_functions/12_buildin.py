def chai_flavor(flavor="masala"):
    """RETURN THE FLAVOR OF CHAI"""
    chai="ginger"
    return flavor

print(chai_flavor.__doc__) #__doc__ this is called as dunder
print(chai_flavor.__name__)

help(len)

def generate_bill(chai=0, samosa=0):
    """
    Calculate the total bill for chai and samosa 
    
    :param chai: Number of chai cups (10 rupees each)
    :param samosa: Number of samosa (10 rupees each)
    :return: (total amount, thank you message)
    """
    total = chai*10 + samosa*15
    return total, "thank you for visiting chaicode.com"