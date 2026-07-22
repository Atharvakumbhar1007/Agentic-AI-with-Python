# List of favourite chai
favourite_chais = [
    "Masala Chai",
    "Green Tea",
    "Masala Chai",
    "Lemon Tea",
    "Green Tea",
    "Elaichi Chai"
]

# Set comprehension: keep only chai names with more than 8 characters
unique_chai = {chai for chai in favourite_chais if len(chai) > 8}

print("Unique Chai:", unique_chai)

# Dictionary of chai recipes
recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"]
}

# Set comprehension to get unique spices
unique_spices = {
    spice
    for ingredients in recipes.values()
    for spice in ingredients
}

print("Unique Spices:", unique_spices)