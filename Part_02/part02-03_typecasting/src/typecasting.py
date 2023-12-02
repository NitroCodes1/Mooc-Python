number = float(input("Please type in a number:"))
decimal = float(number) - int(number)
rounded_decimal = round(decimal, 6)

print("Interger part:", int(number))
print("Decimal part:", float(rounded_decimal))