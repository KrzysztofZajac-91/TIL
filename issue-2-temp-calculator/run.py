textCtoF = "1) Stopnie Celsjusza na Fahrenheita"
textFtoC = "2) Stopnie Fahrenheita na Celsjusza"
order = "Podaj wartość: "

print("Program do konwersji temperatury")
print("Jaką konwersje chcesz wykonać?")
print(textCtoF)
print(textFtoC)

choice = int(input("Wybierz: "))

if choice == 1:
    print(textCtoF[3:])
    number1= float(input(order))
    result1 = number1* 1.8 + 32
    print(number1, "°C to", result1, "°F")

if choice == 2:
    print(textFtoC[3:])
    number2= float(input(order))
    result2 = (number2 - 32) / 1.8
    print(number2, "°F to", result2, "°C")