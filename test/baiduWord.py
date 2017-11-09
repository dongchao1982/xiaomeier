#encoding=utf-8

from aip import AipSpeech
import sys

""" 你的 APPID AK SK """
APP_ID = '10334864'
API_KEY = 'a3oLsPhpPIOYFOmtzatMwmI0'
SECRET_KEY = 'c424091dd2302302c873ac4804570d28'

fileformat = 'wav'

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

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
            
    
