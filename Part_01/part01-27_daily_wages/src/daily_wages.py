h = float(input("Hourly wage:"))
w = int(input("Hours worked:"))
day = input("Day of the week:")

wage = h * w 

if day == 'Sunday':
    wage = wage * 2

print(f"Daily wages: {wage} euros")