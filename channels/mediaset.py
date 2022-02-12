import requests, urllib
result = []
api = "https://static3.mediasetplay.mediaset.it/apigw/nownext/nownext.json"

def get_channels():
    r = requests.get(api).json()["response"]
    stations = r["stations"]
    guides = r['listings']
    
    for s in stations.values():
        channel_name = s["title"]
        if s["callSign"] in guides:
            g = guides[s["callSign"]]
            url=g['tuningInstruction']["urn:theplatform:tv:location:any"][0]["publicUrls"][0]
            try: result.append({"name": channel_name, "url": urllib.request.urlopen(url).geturl()})
            except: pass
    return result
