#! /usr/bin/python
# -*- coding: utf-8 -*-

import urllib,urllib2,os

class dTTS:
    """ dTTS (Baidu Text to Speech): an interface to Baidu's Text to Speech API """
    BAIDU_TTS_URL = 'http://tts.baidu.com/text2audio'
    LANGUAGES = {
        'zh' : 'zh',
        'en' : 'en',
    }

    def __init__(self, text = 'my name is arvin', lang = 'en'):
        if lang.lower() not in self.LANGUAGES:
            raise Exception('Language not supported: %s' % lang)
        else:
            self.lang = lang.lower()

        if not text:
            raise Exception('No text to speak')
        else:
            self.text = text.replace('\n', '').replace('\r', '').strip()

    def save(self, savefile = 'voice.mp3'):
        """ Do the Web request and save to `savefile` """
        with open(savefile, 'wb') as f:
            self.write_to_fp(f)
        return savefile

    def write_to_fp(self, fp):
        """ Do the Web request and save to a file-like object """
        url = self.BAIDU_TTS_URL
        parameters = {"lan": self.lang, "ie": "UTF-8", "text": self.text, "spd": "4"}
        data_encode = urllib.urlencode(parameters)
        url += "?"+data_encode
        try:
            res = urllib2.urlopen(url)
            fp.write(res.read())
        except Exception as e:
            raise

if __name__ == "__main__":
    #pass
    while True:
        txt = raw_input("\nEnter En Text:\n\n")
        if txt == 'qt':
            print "\nbye!\n"
            break;
        dtts = dTTS(txt)
        #brew install sox
        os.system('clear&play %s' % dtts.save())
        print '\n'
