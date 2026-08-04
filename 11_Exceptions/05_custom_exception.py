def brew_chai(flavor):
    if flavor not in ["masala", "ginger", "elaichi"]:
        raise ValueError("Unsupported chai flavor.")

    print(f"Brewing {flavor} chai")


# Example usage
brew_chai("masala")    # Brewing masala chai
brew_chai("ginger")    # Brewing ginger chai
brew_chai("elaichi")   # Brewing elaichi chai
# brew_chai("mint")    # Raises ValueError