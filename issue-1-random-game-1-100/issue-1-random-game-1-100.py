from random import randint
randomNumber = randint(0, 100)
shot = 101

print("Została wylosowana liczba z przedziału 0-100.")
text = "Zgadnij jaka to liczba: "

while True:
    shot = int(input(text))
    text = "Zgadnij jeszcze raz: "
    if shot > randomNumber:
        print("Za duża liczba. ")
    if shot < randomNumber:
        print("Za mała liczba. ")
    if shot == randomNumber:
        break

print("Tak! Brawo!")
