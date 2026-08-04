chai_menu = {"masala": 30, "ginger": 40}
try:
    chai_menu["elaichi"]
except KeyError:
    print("The key that are tryong to access does not exists")

print("Hello chai code")