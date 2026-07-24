class ChaiUitls:
    
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]
    
raw = "Water , milk ,  ginger , honey"

cleaned = ChaiUitls.clean_ingredients(raw)
print(cleaned)
