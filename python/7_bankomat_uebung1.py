balance = 0
while True:
    command = input("Bitte wähle die Aktion: Einzahlen, Auszahlen, Kontostand, Beenden")
    if command == "Einzahlen":
        addBal = int(input("Bitte Betrag eingeben"))
        balance += addBal
    elif command == "Auszahlen":
        remBal = int(input("Bitte Betrag eingeben"))
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
