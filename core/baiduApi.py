#encoding=utf-8

import ConfigParser
from aip import AipSpeech
import subprocess
import os
import hashlib
from synthesisModel import synthesisModel

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

class baiduAPI(object):

    db_conn = None

    def __init__(self):
        cf = ConfigParser.ConfigParser()
        cf.read("../data/config.txt")
        self.APP_ID = cf.get("baidu","app_id")
        self.API_KEY = cf.get("baidu","api_key")
        self.SECRET_KEY = cf.get("baidu","secret_key")
        self.model = synthesisModel()

    def synthesis(self,words):
        if len(words) >= 1024:
            return False

        #从数据库中查找
        filename = self.model.find(words)
        if filename!=None:
            self.model.updateHit(words)
            return filename

        aipSpeech = AipSpeech(self.APP_ID, self.API_KEY, self.SECRET_KEY)
        result = aipSpeech.synthesis(words,'zh',1,{
            'vol':10,'per':4
            })
        if not isinstance(result, dict):
            name = hashlib.md5(words).hexdigest()
            filename =  name + ".wav"
            tempfilename = "../temp/" + name + ".mp3"
            with open(tempfilename,'wb') as f:
                f.write(result)
                subprocess.call(['ffmpeg', '-i', tempfilename,'-y',"../data/voice/"+filename])
                os.remove(tempfilename)
                #更新数据库
                self.model.insert(words,filename)
                return filename
            return None
        else:
            return None

    def asr(self,filename):
        aipSpeech = AipSpeech(self.APP_ID, self.API_KEY, self.SECRET_KEY)
        return aipSpeech.asr(get_file_content(filename), 'wav', 16000, {'lan': 'zh',})


