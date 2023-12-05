import string

alphabet = list(string.ascii_lowercase) + ["\n"]


def filtrer(texte):
    longueur = len(texte)
    texte_filtre = ""
    for x in range(0, longueur):
        if not (texte[x] in alphabet):
            texte_filtre += texte[x]

    return texte_filtre


file = open("input.txt", "r")

data = []
line = file.readline()
while line:
    data.append(line)
    line = file.readline()

file.close()


somme = 0
for line in data:
    texte_filtre = filtrer(line)
    somme += int(texte_filtre[0] + texte_filtre[len(texte_filtre) - 1])


print(somme)
