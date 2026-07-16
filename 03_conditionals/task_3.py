cup = input("Choose your cup size (small/medium/large):").lower()
if cup == "small":
    print("Price is 10 Rupees")
elif cup == "medium":
    print("Price is 15 Rupees")
elif cup == "large":
    print("Price is 20 Rupees")
else:
    print("Unknown cup size")