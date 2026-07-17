flavours = ["Ginger", "Out of Stock", "Discontinued", "Tulsi"]

for flavour in flavours:
    if flavour == "Out of stack":
        continue
    if flavour == "Discontinued":
        break
    print(f"{flavour} item found")
    
print(f"Out side of loop")