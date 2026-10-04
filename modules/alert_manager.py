from pygame import mixer

def play_voice_alert():

    mixer.init()

    mixer.music.load("alert.mp3")

    mixer.music.play()