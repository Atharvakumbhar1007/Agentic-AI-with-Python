def serve_chai(flavor):
    try:
        print(f"preparing {flavor} chai...")
        if flavor == "unknown":
            raise ValueError("We dont know that flavor")
    except ValueError as e:
        print("Erroe: ",e)
    else:
        print(f"{flavor} chai is servered")
    finally:
        print("Next customer please")
        
serve_chai("masala")
serve_chai("unknown")