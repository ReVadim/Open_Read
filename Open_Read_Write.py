cook_book = {}
cook = {}
cook_list = []

with open('recipes.txt', 'r') as file:
    text = file.readlines()

for line in text:
    line = line.rstrip().split()
    if '|' not in line and [a for a in line if a.isalpha() is True]:
        cook_list = []
        cook_book[str(' '.join(line))] = cook_list

    elif '|' in line:
        line = [a for a in line if a != '|']
        cook = {'ingredient_name': ' '.join(line[:-2]), 'quantity': line[-2], 'measure': line[-1]}
        cook_list.append(cook)


for x, y in cook_book.items():
    print(x, y)

