#encoding=utf-8

from aip import AipSpeech
import subprocess
import sys

""" 你的 APPID AK SK """
APP_ID = '10334864'
API_KEY = 'a3oLsPhpPIOYFOmtzatMwmI0'
SECRET_KEY = 'c424091dd2302302c873ac4804570d28'

filename = 'tempAuido.mp3'
outfilename = 'tempAuido.wav'

def words2sound(words):
    if len(words) >= 1024:
        return False
    
    aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    result = aipSpeech.synthesis(words,'zh',1,{
        'vol':10,'per':4
        })
    if not isinstance(result, dict):
        with open(filename,'wb') as f:
            f.write(result)
    else:
        return False
    return True


if __name__=="__main__":
    if len(sys.argv) >= 2:
        if words2sound(sys.argv[1]):
            subprocess.call(['ffmpeg', '-i', filename,'-y',outfilename])
    
