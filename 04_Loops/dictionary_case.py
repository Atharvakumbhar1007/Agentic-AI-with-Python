users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 150, "coupon": "P10"},
    {"id": 3, "total": 80, "coupon": "P50"},
]

discounts = {
    "P20": (0.2, 0),   # 20% discount
    "P10": (0.1, 0),   # 10% discount
    "P50": (0, 10),    # Fixed ₹10 discount
}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    discount = user["total"] * percent + fixed

    print(
        f"User {user['id']} paid ₹{user['total']} and got "
        f"a discount of ₹{discount} for the next visit."
    )