print("Program do konwersji temperatury")
print("Jaką konwersje chcesz wykonać?")
print("1) Stopnie Celsjusza na Fahrenheita")
print("2) Stopnie Fahrenheita na Celsjusza")

choice = int(input("Wybierz: "))
inputTemperature = float(input("Podaj wartość: "))

if choice == 1:
    conversionResult = inputTemperature * 1.8 + 32
    print("{}°C to {}°F".format(inputTemperature, conversionResult))
elif choice == 2:
    conversionResult = (inputTemperature - 32) / 1.8
    print("{}°F to {}°C".format(inputTemperature, conversionResult))
