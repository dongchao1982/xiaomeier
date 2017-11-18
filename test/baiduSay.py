#encoding=utf-8

from aip import AipSpeech
import subprocess
import sys
import ConfigParser

cf = ConfigParser.ConfigParser()
cf.read("../data/config.txt")

APP_ID = cf.get("baidu","app_id")
API_KEY = cf.get("baidu","api_key")
SECRET_KEY = cf.get("baidu","secret_key")

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
    
