import pandas as pd

inventory = pd.DataFrame({
    "item":["Laptop","Mouse","Keyboard","Monitor"],
    "price":[1200.0,25.5,75.0,300.0],
    "Stock":[15,120,50,30]

})

total_value = (inventory["price"] / inventory["Stock"]) * 100
print(inventory)