import json

def diction():
    fileway = input('Напишите путь до файла, \n') + '/profession'
    global dictions
    with open(fileway, 'r', encoding='utf-8') as t:
        text = t.read()
        items = json.loads(text)
    id_list = []
    name_list = []
    for i in items:
        for id in i['specializations']:
            id_list.append(id["id"])

    for i in items:
        for id in i['specializations']:
            name_list.append(id["name"])

    dictions = dict(zip(name_list, id_list))
    print(dictions)

diction()




