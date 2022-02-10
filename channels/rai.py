import requests

def get_channels():
    result = []
    data = requests.get("http://www.rai.it/dl/RaiPlay/2016/PublishingBlock-9a2ff311-fcf0-4539-8f8f-c4fee2a71d58.html?json").json()
    for channel in data["dirette"]:
        channel_name = channel["channel"].replace("piu", "+")
        url = channel["video"]["contentUrl"]
        result.append({"name": channel_name, "url": url})
    return result

print(get_channels())