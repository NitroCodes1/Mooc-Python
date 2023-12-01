faren  = int(input("Please type in a temprature (F):"))
celcius = (faren - 32) * 5 / 9

print(f"{faren} degrees Fahrenheit equals {celcius} degrees Celsius")

if celcius < 0:
    print("Brr! It's cold in here!")
