# Listor är en lista över värden som man samlar ihop
# Här är tillexempel en lista över betyg man kan få

betyg = ["A", "B", "C", "D", "E", "F"]
print(f"Här är listan: {betyg}")
print(f"Här är första värdet i listan {betyg[0]}")
print(f"Här är andra värdet i listan {betyg[1]}")
print(f"Här är sista värdet i listan {betyg[-1]}")

print("---------------------------------------------------------")
# Vad kan man göra med detta då
# Jo att samla ihop värden kan ofta vara bra, tillexempel kan vi
# ta fram ett random betyg

import random
print(f"Ditt betyg i kursen blir: {random.choice(betyg)}")

# Här kommer jag försöka förklara vad det är som händer
#
# import random
# Här laddar vi in random-biblioteket. Det är alltså kod som någon
# annan har skrivit som vi kan använda
#
# print(f"Ditt betyg i kursen blir: {random.choice(betyg)}")
# ^
# Vi börjar med att printa

# print(f"Ditt betyg i kursen blir: {random.choice(betyg)}")
#                                    ^
# Vi börjar med att kalla på random-biblioteket
# print(f"Ditt betyg i kursen blir: {random.choice(betyg)}")
#                                           ^
# Vi kallar på choice funktionen. choice funktionen vill ha en lista
# och där skriver vi in vår lista som heter betyg


print("---------------------------------------------------------")
# Om vi ska lägga till något i listan använder vi något som heter append
betyg.append("A+")
print(f"Här är listan: {betyg}")
# Som ni ser hamnar det nya värdet längst bak

# Att ta bort något gör vi med remove
betyg.remove("F")
print(f"Här är listan: {betyg}")

# Man kan också använda pop för att ta bort något på en specifik plats
print(f"Denna kommer försvinna {betyg[2]}")
betyg.pop(2)
print(f"Här är listan: {betyg}")

