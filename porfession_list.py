import requests

def fetch(url, params):
    headers = params["headers"]
    body = params['body']
    if params["method"] == "GET":
        return requests.get(url, headers=headers)
    if params["method"] == 'POST':
        return requests.post(url, headers=headers, data=body)

professions = fetch("https://api.hh.ru/specializations", {
  "headers": {
    "User-Agent": "MyApp/1.0"
  },
  "body": None,
  "method": "GET"
})
# проверка подключения
# print(professions.status_code)

for i in professions.json():
    for id in i['specializations']:
        print(id['id'])
