with open('1.txt', 'r') as f1, open('2.txt', 'r') as f2, open('3.txt', 'r') as f3:
    file1 = f1.readlines()
    file2 = f2.readlines()
    file3 = f3.readlines()

find_sequence = {'1.txt': [len(file1), file1], '2.txt': [len(file2), file2], '3.txt': [len(file3), file3]}

for_sort = list(find_sequence.values())
for_sort.sort()
for x in for_sort:
    count = 0
    for key, items in find_sequence.items():
        if x[0] in items:
            new_file1 = open('new_file1.txt', 'a+')
            new_file1.write(str(f'\n{key}\n'))
            new_file1.write(str(f'{x[0]}\n'))

    for y in x[-1]:
        count += 1
        for key, items in find_sequence.items():
            if x[0] in items:
                new_line = f'Строка номер {count} из файла {key} ' + y
                new_file1 = open('new_file1.txt', 'a+')
                new_file1.write(new_line)
