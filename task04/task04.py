import os

def calculeaza_dimensiune_subdirectoare(director):
    dimensiune_totala = 0
    for radacina, directoare, fisiere in os.walk(director):
        for subdirector in directoare:
            cale_subdirector = os.path.join(radacina, subdirector)
            #concateneaza mai multe cai intr-una singura
            if os.path.isdir(cale_subdirector):
                dimensiune_subdirector = calculeaza_dimensiune_subdirectoare(cale_subdirector)
                dimensiune_totala += dimensiune_subdirector
                print(dimensiune_subdirector,end = ' ')
        for fisier in fisiere:
            cale_fisier = os.path.join(radacina, fisier)
            dimensiune_totala += os.path.getsize(cale_fisier) #Dimensiunea fișierelor este obținută utilizând
    return dimensiune_totala

director_task04 = "task04"
dimensiune_totala = calculeaza_dimensiune_subdirectoare(director_task04)
print("Dimensiunea totală a subdirectoarelor din directorul task04 este:", dimensiune_totala, "bytes")
