a = "1) Stopnie Celsjusza na Fahrenheita"
b = "2) Stopnie Fahrenheita na Celsjusza"
c = "Podaj wartość:"

print("Program do konwersji temperatury")
print("Jaką konwersje chcesz wykonać?")
print(a)
print(b)
print("Wybierz:")

x = input()
x = int(x)

if x == 1:
    print(a[3:])
    print(c)
    y = input()
    y = float(y)
    result1 = y * 1.8 + 32
    print(y, "°C to", result1, "°F")

if x == 2:
    print(b[3:])
    print(c)
    z = input()
    z = float(z)
    result2 = (z - 32) / 1.8
    print(z, "°F to", result2, "°C")