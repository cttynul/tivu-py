def get_channels():
    # troppo pigro per reversare le api al momento 
    result = [
        {"name":"Real Time", "url":"https://sbshdlu5-lh.akamaihd.net/i/sbshdl_4@810998/master.m3u8"}, 
        {"name":"DMAX", "url":"https://sbshdlu5-lh.akamaihd.net/i/sbshdl_5@825063/master.m3u8"}, 
        {"name":"Giallo", "url":"https://sbshdlu5-lh.akamaihd.net/i/sbshdl_2@810996/master.m3u8"}, 
        {"name":"Food Network", "url":"https://sbshdlu5-lh.akamaihd.net/i/sbshdl_6@1000854/master.m3u8"}, 
        {"name":"Motor Trend", "url":"https://sbshdlu5-lh.akamaihd.net/i/sbshdl_1@810993/master.m3u8"}
        ]
    return result

print(get_channels())