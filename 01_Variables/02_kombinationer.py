# Vi börjar med en vanlig textVariabel
textVariabel = "text"
print(f"{textVariabel}")

# textVariabel += 42
# Så här kan man INTE göra, man kan inte lägga till en int på en string

# Vi testar skapa en intvariabel som vi kan lägga till
intVariabel = 42

# textVariabel += intVariabel
# Såhär får man INTE heller göra

textVariabel += "42"
print(f"Såhär kan man dock göra: {textVariabel}")

textVariabel += str(intVariabel)
print(f"Såhär kan man också genom att gör om int till string: {textVariabel}")

# Vi gör en floatvariabel också
floatVariabel = 3.14

# Vi kan addera en float på en int, för båda är ett "tal"
intVariabel += floatVariabel
print(f"Intvariabel efter addering {intVariabel}")
# Men tänk på att int variabeln nu är en float
print(f"Typen på intVariabel: {type(intVariabel)}")

