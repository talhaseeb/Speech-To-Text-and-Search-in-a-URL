import speech_recognition as sr
import webbrowser as wb

r1 = sr.Recognizer()
r2 = sr.Recognizer()

with sr.Microphone() as source:
    print('[say video to search on youtube')
    print('speak now')
    audio = r2.listen(source)

if 'video' in r1.recognize_google(audio):
    r1 = sr.Recognizer()
    url = 'https://www.youtube.com/results?search_query='
    with sr.Microphone() as source:
        print('search whatever you want')
        audio = r1.listen(source)

    try:
        get = r1.recognize_google(audio)
        print(get)
        wb.get().open_new(url+get)
    except sr.UnknownValueError:
        print('error')
    except sr.RequestError as re:
        print('failed'.format(re))