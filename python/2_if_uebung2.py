from random import randrange
i1 = randrange(100)
i2 = randrange(100)

if i1 < i2 and i1 < 50:
    print("Zahl 1 ist kleiner als Zahl 2 und Mini")

if i1 < 30 or i2 < 30:
    print("Einer der beiden Zahlen ist kleiner als 30")

if i1 < 50 and not i2 == 50:
    print("Zahl 1 ist kleiner als 50, und Zahl 2 ist kein 50er")