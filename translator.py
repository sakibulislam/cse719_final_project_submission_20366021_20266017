import http.client
import json

import requests
from googletrans import Translator

class Translator:
    def __init__(self):
        pass
    try:
        def isEnglish(self, s):
            try:
                s.encode(encoding='utf-8').decode('ascii')
            except UnicodeDecodeError:
                return False
            else:
                return True


        #google input
        def request_bangla(self, word):
            conn = http.client.HTTPSConnection('inputtools.google.com')
            conn.request('GET', '/request?text=' + word + '&itc=bn-t-i0-und&num=5&cp=0&cs=1&ie=utf-8&oe=utf-8&app=test')
            res = conn.getresponse()
            # print(res)
            # exit(1)
            arr = res.read().decode('utf-8')
            data = json.loads(arr)
            return data


        def get_translator(self, banglish_text):

            # text format
            # banglish_text = 'amar naam Sakibul Islam'
            bangla_list = []

            if (self.isEnglish(banglish_text)):

                banglish_text = banglish_text.replace('.', ',')
                banglish_text = banglish_text.replace(' ', '+')
                arr = self.request_bangla(word=banglish_text)
            else:
                bangla_list.append(banglish_text)
            # print(arr)
            comma_count = banglish_text.count(',')
            # print("comma_count", comma_count)
            loop_variable = 0
            if (self.isEnglish(banglish_text)):
                while (loop_variable <= comma_count):
                    # print('target_text:', arr[1][loop_variable][1][0])
                    bangla_list.append(arr[1][loop_variable][1][0])
                    bangla_list.append('.')
                    # print('target_text_type:', type(arr[1][loop_variable][1][0]))
                    # print('translated_text:', get_translated_text(text=arr[1][loop_variable][1][0]))
                    loop_variable += 1
                    if loop_variable == comma_count + 1:
                        break

            bangla_string = ''.join(bangla_list)

            # bangla lang found
            # eng translation starts
            r = requests.get(
                "https://translation.googleapis.com/language/translate/v2",
                params={
                    "key": 'AIzaSyDEDc3NuuVAxCiXuNdn_Um0PYtCVvwifBY',
                    "q": bangla_string,
                    "target": "en",
                    "alt": "json",
                    "source": "bn"
                }
            )

            arr = r.json()
            # print(arr)
            eng_string = arr['data']['translations'][0].get('translatedText')
            # print(eng_string)

            return eng_string
    except Exception as ex:
        print('Exception: ', ex.with_traceback())
