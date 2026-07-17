name = ["Hitesh", "Ram","Sam","Raj"]
bills = [50,25,150,100]
for name, amount in zip(name, bills):
    print(f"{name} paid{amount} rupees")