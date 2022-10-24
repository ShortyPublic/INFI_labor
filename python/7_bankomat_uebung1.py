balance = 0
while True:
    print("Bitte wähle die Aktion: Einzahlen, Auszahlen, Kontostand, Beenden")
    command = input()
    if command == "Einzahlen":
        print("Bitte Betrag eingeben")
        addBal = int(input())
        balance += addBal
    elif command == "Auszahlen":
        print("Bitte Betrag eingeben")
        remBal = int(input())
        if remBal > balance:
            remBal = balance
        balance -= remBal
        print(remBal, "abgehoben")
        print("Neuer Kontostand:", balance)
    elif command == "Kontostand":
        print("Kontostand", balance)
    else:
        print("Danke, dass Sie unseren Bankomat verwendet haben ;-)")
        break
