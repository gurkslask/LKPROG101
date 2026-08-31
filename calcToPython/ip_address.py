def oktett():
    ip = int(input("Vilken ip????\n"))
    high = 256
    low = -1
    if low < ip < high:
        print("ok")
    elif ip > high:
        print(f"För högt {ip}")
    elif ip < low:
        print(f"För lågt {ip}")

def oktettBin(ipp: int):
    ip = ipp
    high = 256
    low = -1
    if low < ip < high:
        print("ok")
    elif ip > high:
        print(f"För högt {ip}")
    elif ip < low:
        print(f"För lågt {ip}")
    print(bin(ip))
def oktettBinSubb(ipp: int):
    validValues = [0, 128, 192, 224, 240, 248, 252, 254, 255]
    ip = ipp
    high = 256
    low = -1
    if low < ip < high and ip in validValues:
        print("ok")
    elif ip > high:
        print(f"För högt {ip}")
    elif ip < low:
        print(f"För lågt {ip}")
    elif ip not in validValues:
        print(f"Inte valid {ip}")
    print(bin(ip))

ip = int(input("vilken ip?"))
oktettBinSubb(ip)
