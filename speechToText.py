import googletrans
import speech_recognition as sr
from googletrans import Translator
import docx
import importlib;

importlib.reload(googletrans)

def get_translator(english_text):
    translator = Translator()
    # print(translator.detect(english_text))
    result = translator.translate(english_text, src='en', dest='bn')
    return result.text

def write_translated_text(translated_text):
    mydoc = docx.Document()
    mydoc.add_paragraph(str(translated_text))
    mydoc.save("F:/translated_written_file.docx")
try:
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Say Something!')
            audio = r.listen(source)
            # time.sleep(10)
            print("processing....")
            english_text = r.recognize_google(audio)
            bangla_text = r.recognize_google(audio, language='bn-BD')
            print("processing....completed")
            print("audio_voice_to_english_text: " + english_text)
            # print("Bangla: " + bangla_text)
            print('translated_bengali_text:', get_translator(english_text))
            write_translated_text(get_translator(english_text))
            print('Translated Text Saved as Doc file Successfully')
            exit(0)
except Exception as ex:
    print('Exception: ', ex.with_traceback())









