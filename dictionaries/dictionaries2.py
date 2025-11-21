car = {"brand": "Ford", "model": "Mustang", "year": 1964}

model = car.get("model", "N/A")
year  = car.get("year",  "N/A")

print("Model:", model)
print("Year: ", year)
