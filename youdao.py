# -*- coding: utf-8 -*-
#! /usr/bin/env python

import urllib2
import urllib
import simplejson as json
import sys

class YoudaoDic():
    """
    有道词典API
    """
    VERSION = 1.1

    URL = 'http://fanyi.youdao.com/openapi.do'

    KEY_FROM = 'YoudaoDic'

    KEY = '1943349323'

    TYPE = 'data'

    # 可选值xml, json
    DOC_TYPE = 'json'

    def translate(self, text):
        """
        翻译方法，传入要翻译的文本，返回结果字典
        """
        # 参数
        params = {'keyfrom': self.KEY_FROM, 'key': self.KEY, 'type': self.TYPE, 'doctype': self.DOC_TYPE, 'version': self.VERSION ,'q': text}
        request = urllib2.urlopen(self.URL, urllib.urlencode(params))
        data = request.read()
        return json.loads(data)

    def format_for_command(self, text):
        """
        为命令行格式化翻译结果
        """
        data = main(text)
        # TODO：格式化字符串
        if data:
            print '有道翻译：'
            print '\t原文本：', data.get('query', text) 
            translation = data.get('translation', None) 
            if translation: 
                for t in translation:
                    print '\t翻  译：', t
            else:
                '未找到该词'

def main(text):
    if text and text.strip() != '':
        return YoudaoDic().translate(text)

if __name__ == '__main__':
    if sys.argv and len(sys.argv) >= 2:
        YoudaoDic().format_for_command(sys.argv[1])
    else:
        print '没有参数哦，亲!'
