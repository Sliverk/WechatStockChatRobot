from wxpy import *
bot = Bot()

# my_friend = bot.friends().search('beatifiC.H')[0]
# my_friend = bot.friends().search('河流呀')[0]
my_friend = bot.friends().search('Melody')[0]
# my_friend = bot.friends().search('去散步了')[0]
# my_friend = bot.friends().search('雪落涟漪')[0]
# my_friend = bot.friends().search('闭嘴')[0]


print ('Found!!!!')
my_friend.send('你已连接至股价查询服务，发送语音或文字即可体验。')
my_friend.send('支持查询的公司有：苹果，百度，微软，特斯拉，谷歌，阿里，创梦天地，拼多多，迅雷，京东，途牛。')
my_friend.send('支持查询的数据有：股价，开盘价，最高价，最低价，成交量，股息率。')


import time
myself = bot.self
bot.file_helper.send('I AM RUNNING AT {}'.format( time.asctime(time.localtime(time.time()) )))


######################################## WATSON SPEECH TO TEXT ####################################
from watson_developer_cloud import SpeechToTextV1
from os.path import join, dirname
import json

speech_to_text = SpeechToTextV1(
    username='8fb8c901-623c-4f95-8d36-b666c0c22f67',
    password='5VTZmXyJv0lc')

def WATSON_Speech2Text(file) :
    with open(join(dirname(__file__), './', file),
                'rb') as audio_file:
        speech_recognition_results = speech_to_text.recognize(
            audio=audio_file,
            content_type='audio/mpeg',
            model='zh-CN_NarrowbandModel',
            interim_results=False,
            keywords=['colorado', 'tornado', 'tornadoes'],
            keywords_threshold=0.5,
            max_alternatives=3)
    if(speech_recognition_results['results'] == []):
        print("Nothing to recognize")
        return
    speech_text = speech_recognition_results['results'][0]['alternatives'][0]['transcript']
    # print(speech_text)
    return speech_text

######################################## BAIDU TRANSLATE ####################################
### NOT USED ###

import http.client as httplib
import hashlib
import urllib
import random

appid = '20180806000191881' #你的appid
secretKey = 'oIJwDkgQVW5FSTMk2ij2' #你的密钥

'''
# Decapated
def BAIDU_Translate(q, fromLang, toLang) : 
    httpClient = None
    myurl = '/api/trans/vip/translate'
    # q = 'apple'
    # fromLang = 'en'
    # toLang = 'zh'
    salt = random.randint(32768, 65536)

    sign = appid+q+str(salt)+secretKey
    m1 = hashlib.md5.new()
    m1.update(sign)
    sign = m1.hexdigest()
    myurl = myurl+'?appid='+appid+'&q='+urllib.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign

    httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
    httpClient.request('GET', myurl)
 
    #response是HTTPResponse对象
    response = httpClient.getresponse()
    a = response.read()
    print (a['trans_result'][0]['dst'][0])
    # print (response.read())
    return a['trans_result'][0]['dst'][0]

    if httpClient:
        httpClient.close()
'''


######################################## WATSON TRANSLATE ####################################
### NOT USED ###

import json
from watson_developer_cloud import LanguageTranslatorV3

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    iam_api_key='CG4Ujv52WV9_Q7LTIxBz7eDRHZEizamQ_1TKcNErKRMQ')

def WATSON_Translate(text, model_id) : 
    translation = language_translator.translate(
        text=text,
        model_id=model_id)
    # print(json.dumps(translation, indent=2, ensure_ascii=False))
    return translation['translations'][0]['translation']


######################################## WATSON ASSISTANT ####################################
### NOT USED ###

import json
import watson_developer_cloud

assistant = watson_developer_cloud.AssistantV1(
    username='c701e0e4-1071-475d-9fed-4c6f4dc44820',
    password='Wq2wUmuMo3tK',
    version='2018-07-10'
)

def WATSON_Assistant(text) :
    response = assistant.message(
        workspace_id='fba62a20-bfea-45df-83b2-9aa4f4acbc2e',
        input={
            'text': text
        }
    )

    # print(json.dumps(response, indent=2))
    # print (response['output']['text'][0])
    return response['output']['text'][0]


######################################## SPACY NLP ####################################
### NOT USED ###
'''
import spacy
nlp = spacy.load("en_core_web_md")
COMPANY_NAME = ['Apple', 'Baidu', 'Microsoft', 'Tesla', 'Google']

def SPACY_Nlp(text) :
    global nlp
    doc = nlp(text)
    for ent in doc.ents:
        print(ent.label_, ent.text)
        if ent.text in COMPANY_NAME :
            return ent.text
    return None
'''

######################################## ROBINHOOD STOCK ####################################

# import requests

# def ROBINHOOD_SearchStockPrice(Company) :
#     if Company == '苹果' :
#         url = 'https://api.robinhood.com/quotes/AAPL/'
#     elif Company == '百度' :
#         url = 'https://api.robinhood.com/quotes/BIDU/'
#     elif Company == '微软' : 
#         url = 'https://api.robinhood.com/quotes/MSFT/'
#     elif Company == '谷歌' :
#         url = 'https://api.robinhood.com/quotes/GOOG/'
#     elif Company == '特斯拉' :
#         url = 'https://api.robinhood.com/quotes/TSLA/'
    
#     r = requests.get(url)
#     print ('status code:', r.status_code)
#     response_dict = r.json()
#     print ("outcome:", response_dict)
#     return response_dict['last_trade_price']

import requests

def ROBINHOOD_SearchStockPrice(Postfix, Company, Term) :
    url = 'https://api.robinhood.com/{}/{}/'.format(Postfix, Company)    
    r = requests.get(url)
    # print ('status code:', r.status_code)
    response_dict = r.json()
    # print ("outcome:", response_dict)
    return response_dict['{}'.format(Term)]


######################################## FIND KEYWORD ####################################

def MY_KeywordProcess(text):
    COMPANY_NAME = ['苹果', '百度', '微软', '特斯拉', '谷歌', '阿里', '创梦天地', '拼多多', '迅雷', '京东', '途牛']
    COMPANY_CODE = ['AAPL', 'BIDU', 'MSFT', 'TSLA', 'GOOG', 'BABA', 'DSKY', 'PDD', 'XNET', 'JD', 'TOUR']

    STOCK_TERM = ['股价','开盘价','最高价','最低价','成交量','股息率']
    STOCK_TERM_CODE = ['last_trade_price', 'open', 'high', 'low', 'volume', 'pe_ratio']
    cpn_name = '空'
    index = 0
    for name in COMPANY_NAME:
        if text.find(name) != -1:
            cpn_name = name
            break
        index = index + 1
    cpn_code = COMPANY_CODE[index]

    index = 0
    for name in STOCK_TERM:
        if text.find(name) != -1:
            term_name = name
            break
        index = index + 1
    term_code = STOCK_TERM_CODE[index]

    if term_code == 'last_trade_price':
        postfix = 'quotes'
    else:
        postfix = 'fundamentals'
    return cpn_name, term_name, postfix, cpn_code, term_code


######################################## BAIDU SPEECH TO TEXT ####################################

from aip import AipSpeech
import subprocess
import signal
import os
import time
import http.client
import hashlib
import urllib
import random
import json

""" 你的 APPID AK SK """
APP_ID = '11632039'
API_KEY = 'F1tOtB8Z96DE4oaBCdGVvbKE'
SECRET_KEY = 'BqgS5B1L4qE2KvuWS2cRR6rxxyFZvFPN'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

appid = '20180804000191549' #你的appid
secretKey = 'M_QF2liMrYEpd1z1RVzu' #你的密钥

def BAIDU_V2T(filepath):
    if os.path.exists('aa.wav'):
        os.remove('aa.wav')
    os.system("ffmpeg -i aa.mp3 -acodec pcm_s16le -ac 1 -ar 16000 aa.wav")

    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    # print ('Processing...')
    asr_result = client.asr(get_file_content('aa.wav'), 'wav', 16000, {
        'dev_pid': 1536,
    })
    # print ('Done!!!')
    return asr_result['result'][0]

######################################## WXPY WECHAT SERVICE ####################################

# @bot.register()
# def print_others(msg):
#     print(msg)

@bot.register(my_friend)
def reply_my_friend(msg):
    if msg.type == 'Recording' :
        # Step 1 : Save the Voice
        msg.get_file(save_path = './aa.mp3')
        print ('Speech Has Been Saved.')
        
        # Step 2 : Transform to Text
        instrument = BAIDU_V2T('aa.mp3')
        print ('instrument is : ', instrument)
        
        # return 'received:{}'.format(speechtext)

    elif msg.type == 'Text' :
        instrument = msg.text
    else :
        return '我是机器人，你在搞毛啊，重发>_<'


    # Step 4 : Keyword Process
    cpn_name, term_name, postfix, cpn_code, term_code = MY_KeywordProcess(instrument)
    print (type(term_name))
    if cpn_name == '空':
        return '对不起，请您重新发送一遍。'

    # Step 5 : Search for Stock Price
    Result = ROBINHOOD_SearchStockPrice(postfix, cpn_code, term_code)
    
    return '{}的{}是：${}'.format(cpn_name, term_name, Result)
    



embed()