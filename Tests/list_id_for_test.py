import json

def fetch(dicionary, dictions):
    for i in dicionary:
        for id in i['specializations']:
            try:
                if float(id["id"]) is not False:
                    dictions.append(id["id"])
            except ValueError:
                print('Найдено не числовое значение: ' + id['id'])
    return dictions


with open('profession1', 'r', encoding='utf-8') as t:
    text = t.read()
    items = json.loads(text)

dictor = []
print(fetch(items, dictor))
