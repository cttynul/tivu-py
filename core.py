import os
lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lib')
os.environ['PATH'] = lib_path + os.pathsep + os.environ['PATH']
from lib import mpv

def initialize_player():
    player = mpv.MPV(input_default_bindings=True, input_vo_keyboard=True, osc=True, ytdl=False)
    return player

def play_m3u(url, player):
    player.play(url)
    player.wait_for_playback()

def main():
    player = initialize_player()
    player.play("https://live2-mediaset-it.akamaized.net/content/hls_h0_clr_vos/live/channel(r4)/index.m3u8")
    player.wait_for_playback()