import json

# read `expenses.json`
with open("expenses.json","r") as f:
    d=json.load(f)

pet_store_items = d["pet store"]
total=0
for item in pet_store_items:
    total+=item["price"]

# get and print total "price" for all expenses at the "pet store"
print(total)