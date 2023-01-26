import json

def fetch(dicionary, dictions):
    for i in dicionary:
        for id in i['specializations']:
            dictions.append(id["id"])
    return dictions

with open('profession', 'r', encoding='utf-8') as t:
    text = t.read()
    items = json.loads(text)

dictor = []
print(fetch(items, dictor))
