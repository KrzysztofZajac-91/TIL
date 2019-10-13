from sys import exit


class WrongChoiceException(Exception):
    pass


def conversion_selection():
    entered_choice = int(input("Wybierz: "))
    if entered_choice > 5 or entered_choice < 1:
        raise WrongChoiceException
    return entered_choice


def enter_speed():
    entered_speed = float(input("Podaj wartość: "))
    return entered_speed


def conversion_list():
    print("1) m/s na km/h")
    print("2) km/h na m/s")
    print("3) mile/h na km/h")
    print("4) km/h na mile/h")
    print("5) km/h na procent prędkości światła w próźni")


def conversion(conversion_choice, input_speed):
    if conversion_choice == 1:
        conversion_result = input_speed * 3.6
        return print("{} m/s to {} km/h".format(input_speed, conversion_result))
    elif conversion_choice == 2:
        conversion_result = input_speed / 3.6
        return print("{} km/h to {} m/s".format(input_speed, conversion_result))
    elif conversion_choice == 3:
        conversion_result = input_speed * 1.609344
        return print("{} mile/h to {} km/h".format(input_speed, conversion_result))
    elif conversion_choice == 4:
        conversion_result = input_speed / 1.609344
        return print("{} km/h to {} mile/h".format(input_speed, conversion_result))
    elif conversion_choice == 5:
        conversion_result = input_speed * 100 / 1079252849
        return print("{} km/h to {}% prędkości światła w próźni".format(input_speed, conversion_result))


print("Program do konwersji prędkości w różnych jednostkach.")
while True:
    print("Jaką konwersje chcesz wykonać?")
    conversion_list()
    try:
        conversion(conversion_selection(), enter_speed())
    except ValueError:
        print("Nieprawidłowa wartość")
        continue
    except WrongChoiceException:
        print("Nieprawidłowa wartość. Wybierz spośród poniższych opcji.")
        continue
    while True:
        closing_decision = input("Czy zakończyć program ([T]ak/[N]ie)? ")
        if closing_decision == "T" or closing_decision == "t" or closing_decision == "Tak" or closing_decision == "tak":
            exit(0)
        elif closing_decision == "N" or closing_decision == "n" or closing_decision == "Nie" or \
                closing_decision == "nie":
            break
        else:
            print("Wpisz T lub N")
