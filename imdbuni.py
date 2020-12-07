import http.client

conn = http.client.HTTPSConnection("imdb8.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "390eb3d922msh2c82861713f4c28p1ee060jsnd27953c51187",
    'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }

conn.request("GET", "/title/find?q=game%20of%20thr", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))