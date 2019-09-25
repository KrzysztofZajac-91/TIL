print("Program do konwersji prędkości w różnych jednostkach.")


def conversion_list():
    print("1) m/s na km/h")
    print("2) km/h na m/s")
    print("3) mile/h na km/h")
    print("4) km/h na mile/h")
    print("5) km/h na procent prędkości światła w próźni")


while True:
    print("Jaką konwersje chcesz wykonać?")
    conversion_list()
    conversion_choice = int(input("Wybierz: "))
    input_speed = float(input("Podaj wartość: "))

    if conversion_choice == 1:
        conversion_result = input_speed * 3.6
        print("{} m/s to {} km/h".format(input_speed, conversion_result))

    elif conversion_choice == 2:
        conversion_result = input_speed / 3.6
        print("{} km/h to {} m/s".format(input_speed, conversion_result))

    closing_decision = input("Czy zakończyć program ([T]ak/[N]ie)? ")
    if closing_decision == "T" or closing_decision == "t" or closing_decision == "Tak" or closing_decision == "tak":
        break
