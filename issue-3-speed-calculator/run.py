print("Program do konwersji prędkości w różnych jednostkach.")


def conversion_selection():
    print("1) m/s na km/h")
    print("2) km/h na m/s")
    print("3) mile/h na km/h")
    print("4) km/h na mile/h")
    print("5) km/h na procent prędkości światła w próźni")


while True:
    print("Jaką konwersje chcesz wykonać?")
    conversion_selection()

    closing_decision = input("Czy zakończyć program ([T]ak/[N]ie)? ")
    if closing_decision == "T" or closing_decision == "t" or closing_decision == "Tak" or closing_decision == "tak":
        break
