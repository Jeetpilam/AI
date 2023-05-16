import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("듣고 있어요 : ")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='ko-KR')
        print("나 : {}".format(text))
    except:
        print("죄송하지만 무슨말을 하신건가요?")