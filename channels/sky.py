import requests

def get_channels():
    result = []
    channels = [{"name":"Sky Tg24", "id":"1"}, {"name":"TV8", "id":"7"}, {"name":"Cielo", "id":"2"}]
    for channel in channels: 
        data = requests.get("https://video.sky.it/be/getLivestream?id=" + channel["id"]).json()
        result.append({"name": channel["name"], "url": data["streaming_url"]})
    return result

print(get_channels())