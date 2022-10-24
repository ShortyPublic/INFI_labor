from random import randrange
print("Willkommen zum Würfelspiel, mach dich bereit zum verlieren!")
computer = []
cSum = 0
while len(computer) < 6:
    computer.append(randrange(6) + 1)
    cSum += computer[-1]
print("[1] Ja\n[2] Nein")
start = int(input("Möchtest du starten?"))
if start == 1:
    wuerfe = 6
    pSum = 0
    while wuerfe > 0:
        wuerfe -= 1
        print("Schreibe x zum würfeln")
        play = input()
        if play == 'x':
            wurf = randrange(6) + 1
            pSum += wurf
            print("Du hast eine", wurf, "gewürfelt! Der Computer hat eine", computer[6 - wuerfe - 1], "gewürfelt.")
        else:
            print("Dann nicht, jetzt bin ich beleidigt.")
            break
        if wuerfe == 0:
            if cSum > pSum:
                print("Du hast gegen den Computer verloren. Schade für dich.")
            elif pSum > cSum:
                print("Du hast gegen den Computer gewonnen. Gut gemacht, aber niemand ist stolz auf dich.")
            else:
                print("Fast. Computer und du sind gleich auf.")