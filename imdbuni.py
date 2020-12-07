import http.client

conn = http.client.HTTPSConnection("imdb8.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "",
    'x-rapidapi-host': ""
    }

conn.request("GET", "/title/find?q=game%20of%20thr", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
