import re

file = open("input.txt", "r")

data = []
line = file.readline()

while line:
    data.append(line)
    line = file.readline()

file.close()

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] + [
    str(x) for x in range(0, 10)
]
numbers_correspondace = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def sort_dic(dic):
    # {0: 'one', 3: 'two', 6: '2', 7: '3', 8: '4'}
    sorted_dic = {}
    sorted_key = sorted([x for x in dic])

    index = 0
    for key in sorted_key:
        sorted_dic[index] = dic[key]
        index += 1
    return sorted_dic


def replace_dic(dic):
    replace_dic = {}
    for x in dic:
        value = dic[x]
        for number in numbers_correspondace:
            value = value.replace(number, str(numbers_correspondace[number]))

        replace_dic[x] = value
    return replace_dic


def filtrer(texte):
    texte_filtre = ""
    apparition = {}
    for number in numbers:
        find = [m.start() for m in re.finditer(number, texte)]
        if find != []:
            for x in find:
                apparition[x] = number

    apparition = replace_dic(sort_dic(apparition))

    return [apparition[x] for x in apparition]


somme = 0
for line in data:
    ligne_filtre = filtrer(line)
    somme += int(ligne_filtre[0] + ligne_filtre[len(ligne_filtre) - 1])

print(somme)
