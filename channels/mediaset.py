def get_channels():
    # troppo pigro per reversare le api al momento 
    result = [
        {"name":"Rete 4", "url":"https://live2-mediaset-it.akamaized.net/content/hls_h0_clr_vos/live/channel(r4)/index.m3u8"}, 
        {"name":"Canale 5", "url":"https://live2-mediaset-it.akamaized.net/content/hls_h0_clr_vos/live/channel(c5)/index.m3u8"}, 
        {"name":"Italia 1", "url":"https://live2-mediaset-it.akamaized.net/content/hls_h0_clr_vos/live/channel(I1)/index.m3u8"}, 
        {"name":"Italia 2", "url":"https://live2-mediaset-it.akamaized.net/content/hls_h0_clr_vos/live/channel(I2)/index.m3u8"},
        {"name":"20", "url":"https://live2-mediaset-it.akamaized.net/content/hls_h0_clr_vos/live/channel(lb)/index.m3u8"}, 
        {"name":"Mediaset Extra", "url":"https://live2-mediaset-it.akamaized.net/content/hls_h0_clr_vos/live/channel(kq)/index.m3u8"}, 
        {"name":"Iris", "url":"https://live2-mediaset-it.akamaized.net/content/hls_h0_clr_vos/live/channel(ki)/index.m3u8"}, 
        {"name":"Top Crime", "url":"https://live2-mediaset-it.akamaized.net/content/hls_h0_clr_vos/live/channel(lt)/index.m3u8"}, 
        {"name": "La 5", "url":"https://live2-mediaset-it.akamaized.net/content/hls_h0_clr_vos/live/channel(ka)/index.m3u8"}, 
        {"name":"Focus", "url":"https://live2-mediaset-it.akamaized.net/content/hls_h0_clr_vos/live/channel(fu)/index.m3u8"}, 
        {"name":"Boing", "url":"https://live2-mediaset-it.akamaized.net/content/hls_h0_clr_vos/live/channel(kb)/index.m3u8"}, 
        {"name":"Cartoonito", "url":"https://live2-mediaset-it.akamaized.net/content/hls_h0_clr_vos/live/channel(la)/index.m3u8"}
        ]
    return result

print(get_channels())