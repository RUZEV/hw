import json

def fetch(dicionary, dictions):
    for i in dicionary:
        for id in i['specializations']:
            dictions.append(id["id"])
    print(dictions)


with open('profession', 'r', encoding='utf-8') as t:
    text = t.read()
    items = json.loads(text)
# fetch(items)

key1 = 'Банковское ПО'
key2 = 'ddddddddd'
dictor = []
fetch(items, dictor)