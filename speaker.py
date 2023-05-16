import time, os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

# 음성인식(듣기, STT)
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='ko')
        print('[나도코딩]' +text)
        answer(text)
    except sr.UnknownValueError:
        print('인식 실패')
    except sr.RequestError as e:
        print('요청 실패: {0}'.format(e))
    except Exception as e:
        print(e)

# 대답
def answer(input_text):
    answer_text = ''
    if '안녕' in input_text:
        answer_text = '반갑습니다. 제이핏입니다.'
    elif '날씨' in input_text:
        answer_text = '오늘의 날씨는 화창합니다.'
    elif '기분' in input_text:
        answer_text = '기분이 아주 좋습니다. 주인님도 기분 좋으시나요?'
    elif '고마워' in input_text:
        answer_text = '돕게되어 영광입니다.'
    elif '종료' in input_text:
        answer_text = '다음에 또 뵐께요!'
        stop_listning(wait_for_stop=False)
    else:
        answer_text = '다시 한번 말씀해주세요!'
    speak(answer_text)

# 마이크 열기
r = sr.Recognizer()
m = sr.Microphone()

# 소리내어 읽기 (TTS)
def speak(text):
    print('[인공지능]' + text)
    file_name = 'voice.mp3'
    tts = gTTS(text=text, lang='ko')
    tts.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name):
        os.remove(file_name)


speak('무엇을 도와드릴까요?')
stop_listning = r.listen_in_background(m, listen)

while True:
    time.sleep(0.1)