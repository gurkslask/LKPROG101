# Såhär gör man en textvariabel, kallas för string
textVariabel = "Här är text"
print(f"Här är texten {textVariabel}")
# Här skriver vi ut vilken datatyp
print(f"{type(textVariabel)}")

# Här lägger vi på texten Lars med hjälp av att kopiera textVariabel
textVariabel = textVariabel + "Lars"
print(f"Här är texten efter ändring med tillägg Lars {textVariabel}")
# Här använder vi += operatorn för att lägga till en text
textVariabel += "Kagg"
print(f"Här är texten efter ännu en ändring med tillägg Kagg {textVariabel}")

print("----------------------------------------------------------------")
# Såhär gör men en int variabel, det är alltså heltal utan decimal
intVariabel = 42
print(f"Här är integer {intVariabel}")
print(f"{type(intVariabel)}")

intVariabel = intVariabel + 1
print(f"Här är integer efter addering {intVariabel}")

intVariabel += 1
print(f"Här är integer efter ännu en addering {intVariabel}")

intVariabel -= 2
print(f"Här är integer efter subtraktion {intVariabel}")

intVariabel *= 10
print(f"Här är integer efter multiplikation {intVariabel}")


print("----------------------------------------------------------------")
# Såhär gör man en float, alltså ett tal som har decimal
floatVariabel = 3.14
print(f"Här är float {floatVariabel}")
print(f"{type(floatVariabel)}")

floatVariabel = floatVariabel + 1
print(f"Här är float efter addering {floatVariabel}")
# Talet ser väldigt konstigt ut, och det är sånt som händer när man kör 
# float, för att fixa det ska vi begränsa hur många decimaler som visas
print(f"{floatVariabel:.3}")

floatVariabel += 1
print(f"Här är float efter ännu en addering {floatVariabel:.3}")

floatVariabel -= 2
print(f"Här är float efter subtraktion {floatVariabel:.3}")

floatVariabel *= 10
print(f"Här är float efter multiplikation {floatVariabel:.3}")

print("----------------------------------------------------------------")
# Här printar vi ut resultaten

print(f"Här är texten {textVariabel} \nHär är inten {intVariabel} \nHär är floaten {floatVariabel}")
