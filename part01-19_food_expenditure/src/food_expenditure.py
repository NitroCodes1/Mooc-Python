week = int(input("How many times a week do you eat at the student cafeteria?"))
price = float(input("The price of a typical student lunch?"))
grocery = float(input("How much money do you spend on groceries in a week?"))

daily = ((week*price) + grocery)/7
weekly = ((week*price) + grocery)
print(f"Daily: {daily} euros")
print(f"Weekly: {weekly} euros")