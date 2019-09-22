from random import randint
randomNumber = randint(0, 100)
print("Została wylosowana liczba z przedziału 0-100.")

text = "Zgadnij jaka to liczba: "
shot = int(input(text))
text = "Zgadnij jeszcze raz: "

while True:
    if shot > randomNumber:
        print("Za duża liczba. ")
    if shot < randomNumber:
        print("Za mała liczba. ")
    if shot == randomNumber:
        break
    shot = int(input(text))

print("Tak! Brawo!")
