seat_type = input("Enter seat type (sleeper/AC/general/luxury)").lower()

match seat_type:
    case "sleeper":
        print("sleeper - No AC, beds available")
    case "AC":
        print("AC -comfy ride")
    case "General":
        print("General - cheapest option, no reservation")
    case "luxury":
        print("luxury - all types of comforts")
    case _:
        print("Invalid sear type")