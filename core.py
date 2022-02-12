import os
lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lib')
os.environ['PATH'] = lib_path + os.pathsep + os.environ['PATH']
from lib import mpv
from channels import rai, sky, discovery, plutotv, mediaset

def get_all_channels():
    return [""] + rai.get_channels() + mediaset.get_channels() + sky.get_channels() + discovery.get_channels() + plutotv.get_channels()

def initialize_player():
    player = mpv.MPV(input_default_bindings=True, input_vo_keyboard=True, osc=True, ytdl=True)
    return player

def play_m3u(url):
    player = mpv.MPV(input_default_bindings=True, input_vo_keyboard=True, osc=True, ytdl=True)
    player.play(url)
    player.wait_until_playing()
    #if player.core_shutdown: 
    #    player.termiante()

def choice_channel(channels):
    choice = 999999999999999999999
    while int(choice) not in range(0, len(channels)):
        choice = input("Inserisci il numero del canale che vuoi guardare > ")
    return choice

def play_channel_internal(channels):
    choice = choice_channel(channels)
    if int(choice) == 0: exit(0) 
    else: play_m3u(channels[int(choice)]["url"])

def play_channel_external(channels):
    import subprocess
    process = subprocess.Popen("mpv.exe " + channels[int(choice)]["url"], stdout=subprocess.PIPE, creationflags=0x08000000)
    process.wait()

def menu(channels):
    for i in range(1, len(channels)):
        print("\t[" + str(i) + "] " + channels[i]["name"])
    while 1: play_channel_internal(channels)

def main():
    channels = get_all_channels()
    menu(channels)