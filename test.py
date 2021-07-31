import requests

url = "https://dad-jokes.p.rapidapi.com/random/joke"

headers = {
    'x-rapidapi-key': "609b2ed0c4msh32545e29c993771p14295ejsn49def6017fd8",
    'x-rapidapi-host': "dad-jokes.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)