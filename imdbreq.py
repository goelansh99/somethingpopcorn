import json,requests
import PIL
import io
url = "https://imdb8.p.rapidapi.com/title/auto-complete"

querystring = {"q":"tron"}

headers = {
    'x-rapidapi-key': "390eb3d922msh2c82861713f4c28p1ee060jsnd27953c51187",
    'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# python_dictionary_values = json.loads(response.text)

# print(response.text)
details=response.json()
print(type(details))
# print(details['d'][0])
print(details['d'][0]['y'])
imgurl=details['d'][0]['i']['imageUrl']
print(imgurl)
img = requests.get(imgurl)
print(imgurl)
# image_bytes = io.BytesIO(img.content)

# img = PIL.Image.open(image_bytes)
# img.show()