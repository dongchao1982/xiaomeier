#encoding=utf-8

from aip import AipSpeech
import platform
import pygame

""" 你的 APPID AK SK """
APP_ID = '10334864'
API_KEY = 'a3oLsPhpPIOYFOmtzatMwmI0'
SECRET_KEY = 'c424091dd2302302c873ac4804570d28'


def say(words):
    if len(words) >= 1024:
        return false
    
    aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    result = aipSpeech.synthesis(words,'zh',1,{
        'vol':10,'per':4
        })
    if not isinstance(result, dict):
        with open('tempAuido.mp3','wb') as f:
            f.write(result)


say("你好，戡戡")
strPlatform = platform.system()
if strPlatform == "Linux":
    pygame.mixer.init()
    pygame.mixer.music.load('tempAuido.mp3')
    pygame.mixer.music.play()
