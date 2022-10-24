from random import randrange
print("Willkommen zum Würfelspiel, mach dich bereit zum verlieren!")
computer = []
while len(computer) < 6:
    computer.append(randrange(6) + 1)