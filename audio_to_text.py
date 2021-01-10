import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
 print('Say something!')
 audio = r.listen(source)
 print('processing........')
 text_bengali = r.recognize_google(audio, language='bn-BD')
 text_english = r.recognize_google(audio)


 print("Recognized Audio into english text: " + text_english)
 print("Bangla: " + text_bengali)