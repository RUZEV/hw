import json
def diction(items):
    id_list = []
    name_list = []
    for i in items:
        for id in i['specializations']:
            id_list.append(id["id"])

    for i in items:
        for id in i['specializations']:
            name_list.append(id["name"])

    dictions = dict(zip(name_list, id_list))
    return dictions

with open("profession", 'r', encoding='utf-8') as t:
    text = t.read()
    items = json.loads(text)
    diction(items)




