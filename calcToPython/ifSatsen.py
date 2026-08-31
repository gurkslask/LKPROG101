def lvl1():
    temperature = 20
    larmHigh = 30

    if temperature > larmHigh:
        print("Larm för hög temperatur!")
    else:
        print("OK")

def lvl2():
    larmHigh = 30
    print(f"Larmtemperaturen är inställd på {larmHigh}")
    temperature = int(input("Vad är temperaturen?\n"))

    if temperature > larmHigh:
        print("Larm för hög temperatur!")
    else:
        print("OK")

def lvl3():
    larmHigh = 30
    print(f"Larmtemperaturen är inställd på {larmHigh}")
    temperature = int(input("Vad är temperaturen?\n"))
    sserverRunning = input("Är servrarna igång? (j/n)")

    if sserverRunning == "j":
        serverRunning = True
    else:
        serverRunning = False

    if temperature > larmHigh and serverRunning:
        print("Larm för hög temperatur!")
    else:
        print("OK")

if __name__ == '__main__':
    lvl3()
