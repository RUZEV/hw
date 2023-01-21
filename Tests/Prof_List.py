import json

def diction():
    #fileway = input('Напишите путь до файла: \n') + '/profession'
    global dictions
    with open('profession', 'r', encoding='utf-8') as t:
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
    #print(id_list)
    dictions = dict(zip(name_list, id_list))
    print(dictions['Банковское ПО'])
    print(dictions)
    # return diction

# key1  = 'Банковское ПО'
# key2 = 'абра-кодабра'
# print(dictions['Банковское ПО'])
diction()




