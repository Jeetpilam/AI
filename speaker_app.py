import time
import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import webbrowser
import tkinter as tk


def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='ko')
        conversation.insert(tk.END, '[나도코딩]' + text + '\n')
        answer(text)
    except sr.UnknownValueError:
        conversation.insert(tk.END, '인식 실패\n')
    except sr.RequestError as e:
        conversation.insert(tk.END, '요청 실패: {0}\n'.format(e))
    except Exception as e:
        conversation.insert(tk.END, '{0}\n'.format(e))


def answer(input_text):
    answer_text = ''
    if '안녕' in input_text:
        answer_text = '반갑습니다. 제이핏입니다. 어떤 음악을 찾아드릴까요?'
    elif '음악' in input_text:
        answer_text = '어떤 음악을 듣고 싶으세요?'
    elif '클래식' in input_text:
        answer_text = '클래식 음악을 재생합니다.'
        play_music('https://www.youtube.com/watch?v=sYV-_qwmk9w')
    elif '시티팝' in input_text:
        answer_text = '시티팝 음악을 재생합니다.'
        play_music('https://www.youtube.com/watch?v=0VARIZfDUAI')
    elif '종료' in input_text:
        answer_text = '다음에 또 뵐께요!'
        stop_listening(wait_for_stop=False)
        root.quit()
    else:
        answer_text = '다시 한번 말씀해주세요!'
    conversation.insert(tk.END, '[인공지능]' + answer_text + '\n')
    speak(answer_text)


def speak(text):
    conversation.insert(tk.END, '[인공지능]' + text + '\n')
    file_name = 'voice.mp3'
    tts = gTTS(text=text, lang='ko')
    tts.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name):
        os.remove(file_name)


def play_music(url):
    webbrowser.open_new(url)


root = tk.Tk()
root.title('AI Speaker')

frame = tk.Frame(root)
frame.pack(pady=20)

label = tk.Label(frame, text='아래 버튼을 클릭하세요!', font=('Arial', 20))
label.pack()

button = tk.Button(frame, text='시작하기', font=('Arial', 20), command=lambda: start())
button.pack(pady=20)

conversation = tk.Text(root, width=50, height=10, font=('Arial', 16))
conversation.pack(pady=20)


def start():
    try:
        global r, stop_listening
        r = sr.Recognizer()
        m = sr.Microphone()
        stop_listening = r.listen_in_background(m, listen)
        speak('무엇을 도와드릴까요?')
    except Exception as e:
        print(e)

root.mainloop()