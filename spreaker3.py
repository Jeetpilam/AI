import time
import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import webbrowser

def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='ko')
        print('[나도코딩]' + text)
        answer(text)
    except sr.UnknownValueError:
        print('인식 실패')
    except sr.RequestError as e:
        print('요청 실패: {0}'.format(e))
    except Exception as e:
        print(e)

def answer(input_text):
    answer_text = ''
    if '안녕' in input_text:
        answer_text = '반갑습니다. 제이핏입니다. 문서를 찾아드릴까요?'
    elif '문서' in input_text:
        answer_text = '어떤 문서를 찾고 싶으세요?'
    elif '찬송가' in input_text:
        answer_text = '찬송가를 재생합니다.'
        play_music('https://www.youtube.com/results?search_query=%EC%B0%AC%EC%86%A1%EA%B0%80+2%EC%9E%A5+%ED%94%BC%EC%95%84%EB%85%B8+%EB%B0%98%EC%A3%BC+')
    elif '언어' in input_text:
        answer_text = '언어 번역기를 재생합니다.'
        play_music('https://translate.google.co.kr/?sl=ko&tl=iw&text=ancient&op=translate&hl=ko')
    elif '종료' in input_text:
        answer_text = '다음에 또 뵐께요!'
        stop_listening(wait_for_stop=False)
    else:
        answer_text = '다시 한번 말씀해주세요!'
    speak(answer_text)

def speak(text):
    print('[인공지능]' + text)
    file_name = 'voice.mp3'
    tts = gTTS(text=text, lang='ko')
    tts.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name):
        os.remove(file_name)

def play_music(url):
    webbrowser.open_new(url)

speak('무엇을 도와드릴까요?')
r = sr.Recognizer()
m = sr.Microphone()
stop_listening = r.listen_in_background(m, listen)

while True:
    time.sleep(0.1)