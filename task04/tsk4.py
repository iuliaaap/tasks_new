import os

def calculeaza_dimensiune_subdirectoare(director):
    dimensiune_totala = 0
    for root, dirs, files in os.walk(director):
        for subdir in dirs:
            cale_subdir = os.path.join(root, subdir)
            #concateneaza caile intr-una singura
            if os.path.isdir(cale_subdir):
                #returneaza True daca este director
                dimensiune_subdir = calculeaza_dimensiune_director(cale_subdir)
                dimensiune_totala += dimensiune_subdir
    return dimensiune_totala
def calculeaza_dimensiune_director(director):
    dimensiune_totala = 0

    for f in os.listdir(director):
        cale_fisier = os.path.join(director, f)
        if os.path.isfile(cale_fisier):
            dimensiune_totala += os.path.getsize(cale_fisier) #returneaza dimensiunea in bytes
        elif os.path.isdir(cale_fisier):
            dimensiune_totala += calculeaza_dimensiune_director(cale_fisier)

    return dimensiune_totala

director_task04 = "task04"
dimensiune_totala = calculeaza_dimensiune_subdirectoare(director_task04)
print(f"Dimensiunea ocupată de subdirectoarele din {director_task04}: {dimensiune_totala} bytes")
