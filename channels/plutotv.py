import requests, uuid
result = []
api = "https://api.pluto.tv/"
puid = "sid=" + str(uuid.uuid1().hex) + "&deviceId=" + str(uuid.uuid4().hex)
apiurl = api + "v2/channels.json?" + puid

def get_channels():
    data = requests.get(apiurl).json()
    for d in data:
        channel_name = d["name"]
        url = d["stitched"]["urls"][0]["url"].split("?")[0]
        result.append({"name": channel_name, "url": url})
    return result

print(get_channels())