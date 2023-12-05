import re

file = open("input.txt", "r")

data = []
line = file.readline()
while line:
    data.append(line)
    line = file.readline()

file.close()


def recuperer_couleur(position, tirage):
    pos2 = position - 2

    while (tirage[pos2] != " ") and (tirage[pos2] != ""):
        pos2 -= 1

    return int(tirage[pos2 + 1 : position - 1])


line_data_filtred = []

# Filtring the data
for line in data:
    line = line[line.find(":") + 1 : len(line)]

    position_point_virgule = [i.start() for i in re.finditer(";", line)]

    tirages = []
    precedent = -2
    for x in position_point_virgule:
        tirages.append(line[precedent + 2 : x])
        precedent = x - 1
    tirages.append(line[precedent + 2 : len(line)])

    list_color = []

    for tirage in tirages:
        tirage_sort_position = {"red": -1, "green": -1, "blue": -1}
        for couleur in tirage_sort_position:
            if tirage.find(couleur) != -1:
                tirage_sort_position[couleur] = tirage.find(couleur)

        couleurs = {"red": -1, "green": -1, "blue": -1}

        for couleur in couleurs:
            if tirage_sort_position[couleur] != -1:
                couleurs[couleur] = recuperer_couleur(
                    tirage_sort_position[couleur], tirage
                )
        list_color.append(couleurs)

    line_data_filtred.append(list_color)



def Is_possible(tirage):
    if (tirage["red"] > 12) or (tirage["green"] > 13) or (tirage["blue"] > 14):
        return False
    return True


index = 1
reponse = 0
for line in line_data_filtred:
    possible = True

    for case in line:
        if Is_possible(case) == False:
            possible = False

    if possible == True:
        reponse += index

    index += 1

# print(line_data_filtred)
print(reponse)
