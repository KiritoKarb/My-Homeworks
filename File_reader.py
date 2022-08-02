files_list = {}
for i in range(1, 3+1):
    with open(f'{i}.txt', encoding='utf-8') as file:
        readed_file = file.read()
        line_counter = readed_file.count('\n') + 1
        files_list[line_counter] = {'file name': f'{i}.txt', 'lines': line_counter, 'text': readed_file}

files_list = dict(sorted(files_list.items(), key=lambda x:  x[0]))

with open('final.txt', 'w', encoding='utf-8') as file:
    for item in files_list.values():
        file.write(item['file name'])
        file.write('\n')
        file.write(str(item['lines']))
        file.write('\n')
        file.write(item['text'])
        file.write('\n')