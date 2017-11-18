#encoding=utf-8
import ConfigParser
from aip import AipSpeech
import sys

cf = ConfigParser.ConfigParser()
cf.read("../data/config.txt")

APP_ID = cf.get("baidu","app_id")
API_KEY = cf.get("baidu","api_key")
SECRET_KEY = cf.get("baidu","secret_key")

fileformat = 'wav'

def sound2word(filename):
    aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    return aipSpeech.asr(get_file_content(filename), fileformat, 16000, {'lan': 'zh',})


if __name__=="__main__":
    if len(sys.argv) >= 2:
        result = sound2word(sys.argv[1])
        if result['err_no'] == 0:
            print result['result'][0]
        else:
            print 'error(%d):%s'%(result['err_no'],result['err_msg'])
            
    
