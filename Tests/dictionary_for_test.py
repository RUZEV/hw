import json

def fetch(dicionary, key):
    id_list = []
    name_list = []
    for i in dicionary:
        for id in i['specializations']:
            id_list.append(id["id"])

    for i in dicionary:
        for id in i['specializations']:
            name_list.append(id["name"])
            dictions = dict(zip(name_list, id_list))
    print(dictions[key])
    print(dictions)


with open('profession', 'r', encoding='utf-8') as t:
    text = t.read()
    items = json.loads(text)
# fetch(items)

key1 = 'Банковское ПО'
key2 = 'ddddddddd'

fetch(items, key1)