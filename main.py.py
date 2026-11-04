import random as rand
välkommen = input("Vad heter du? ")

print(f"Hej {välkommen} och välkommen till spelet")

random = rand.randint(1, 10)
tal = int(input("Gissa ett tal mellan 1 och 10 --> "))

if tal == random:
    print("Du gissade rätt")
else:
    print(f"Tyvärr, talet var {random}")

antal_försök = 1

while True:
    if tal == random:
        print(f"Försök {antal_försök}:")
        print("Du gissade rätt")
        break
    if tal != random:
        print(f"Försök {antal_försök}:")
        print("Du gissade fel")
        antal_försök += 1
    tal = int(input("Gissa ett tal mellan 1 och 10 --> "))
    
    

    


