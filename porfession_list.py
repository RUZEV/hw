import requests

def fetch(url, params):
    headers: params["headers"]
    body: params['body']
    if params["method"] == "GET":
        return requests.get(url, headers=headers)
    if params["method"] == 'POST':
        return requests.post(url, headers=headers)

professions = fetch("https://api.hh.ru/specializations", {
  "headers": {
    "User-Agent": "MyApp/1.0"
  },
  "body": None,
  "method": "GET"
})

print(professions.status_code)
print(professions.json())