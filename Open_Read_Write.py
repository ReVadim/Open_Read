cook_book = {}
cook = {}
cook_list = []
sort_dict = {}  # for testing

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


def get_shop_list_by_dishes(dishes, person_count):
    all_sort = {}
    for value in dishes:
        if value in cook_book.keys():
            for title in cook_book[value]:
                name = title.pop('ingredient_name')
                if name in all_sort.keys():
                    title['quantity'] = int(title['quantity']) * person_count + int(all_sort[name]['quantity'])
                    all_sort[name] = title
                    sort_dict[name] = title
                else:
                    title['quantity'] = int(title['quantity']) * person_count
                    all_sort[name] = title
                    sort_dict[name] = title
        else:
            print(value, ' not in cook_book')

    return print(all_sort)


def print_shop_list(some_dict):
    for y, z in some_dict.items():
        print(f'{y} : {z}')


def get_contents(some_dict):
    out = []
    for keys, items in some_dict.items():
        out.append(keys)
    print("Contents:", *out, sep=', ')

# testing area, remove '#':

# """ task-1 """
for x, y in cook_book.items():
    print(x, y)

# """ task-2 """
# get_contents(cook_book)
# get_shop_list_by_dishes(['Шарлотка', 'Морковный пирог', 'Кекс'], 3)
# print_shop_list(sort_dict)
