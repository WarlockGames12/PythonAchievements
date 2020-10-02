naam = input("Wat is jouw naam ")
print("Dus je naam is", naam)


leeftijd = input("Hoe oud ben je? ")
print("Ah, dus je bent", leeftijd, "jaar oud")


woonplaats = input("Welke stad woon je? ")
print("Ah, dus u woont in ", woonplaats)

print("Perfect, dus uw naam is", naam, " ,je bent ", leeftijd, " jaar oud en komt uit", woonplaats)
waar = input("Is dat waar? type ja of nee ")
if waar == "ja":
   print("Perfect")
elif waar == "nee":
   print("Godverdomme")
else: 
   print("Alstublieft type ja of nee")
        