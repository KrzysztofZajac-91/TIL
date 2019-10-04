def conversion_list():
    print("1) m/s na km/h")
    print("2) km/h na m/s")
    print("3) mile/h na km/h")
    print("4) km/h na mile/h")
    print("5) km/h na procent prędkości światła w próźni")


print("Program do konwersji prędkości w różnych jednostkach.")


while True:
    print("Jaką konwersje chcesz wykonać?")
    conversion_list()

    try:
        conversion_choice = int(input("Wybierz: "))
        input_speed = float(input("Podaj wartość: "))
    except ValueError:
        print("Nieprawidłowa wartość")
        continue

    if conversion_choice == 1:
        conversion_result = input_speed * 3.6
        print("{} m/s to {} km/h".format(input_speed, conversion_result))

    elif conversion_choice == 2:
        conversion_result = input_speed / 3.6
        print("{} km/h to {} m/s".format(input_speed, conversion_result))

    elif conversion_choice == 3:
        conversion_result = input_speed * 1.609344
        print("{} mile/h to {} km/h".format(input_speed, conversion_result))

    elif conversion_choice == 4:
        conversion_result = input_speed / 1.609344
        print("{} km/h to {} mile/h".format(input_speed, conversion_result))

    elif conversion_choice == 5:
        conversion_result = input_speed * 100 / 1079252849
        print("{} km/h to {}% prędkości światła w próźni".format(input_speed, conversion_result))

    else:
        print("Nieprawidłowa wartość")
        continue

    closing_decision = input("Czy zakończyć program ([T]ak/[N]ie)? ")
    if closing_decision == "T" or closing_decision == "t" or closing_decision == "Tak" or closing_decision == "tak":
        break
