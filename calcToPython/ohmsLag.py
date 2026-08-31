strom = 10
spanning = 230
resistans = 100

print("Strömmen är ", strom)
print("Spänningen är ", spanning)
print("Resistensen är ", resistans)

# print("Vi räknar ut resistansen som är spänning delat med ström. Uträknad resistans: ", spanning / strom)
val = input("Vad vill du räkna ut?\n1. Ström\n2.Spänning\n3.Resistans\n")
if val == "1":
    print("Strömmen är ", spanning / resistans)
elif val == "2":
    print("Spänningen är ", strom * resistans)
elif val == "3":
    print("Resistansen är ", spanning * strom)
