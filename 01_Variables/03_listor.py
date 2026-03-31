# Listor är en lista över värden som man samlar ihop
# Här är tillexempel en lista över betyg man kan få

betyg = ["A", "B", "C", "D", "E", "F"]

# Vad kan man göra med detta då
# Jo att samla ihop värden kan ofta vara bra, tillexempel kan vi
# ta fram ett random betyg

import random
print(f"Ditt betyg i kursen blir: {random.choice(betyg)}")
