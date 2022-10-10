from random import randrange

# Zahlen addieren
def add(x, y):
    return x + y

print(add(5, 6))

# Zufällige Zahl zwischen 100 und 200
def random100_200():
    return randrange(100) + 100

print(random100_200())

# Zufälliges Wort aus Array
def randomWord(array):
    return array[randrange(len(array))]

print(randomWord(["Fisch", "Computer", "Papierfabrik", "außerordentlich"]))