import random
from gtts import gTTS
from playsound import playsound
import os
import speech_recognition as sr

def speak(string):
    #string='üst düzey rütbeli terimci'
    tts= gTTS(string,lang='tr')
    rand=random.randint(1,10000)
    file='audio-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)
    
speak('bu u  ada am be nim baba am seki iz köşe e kaske tiy le omu uzunda sakosu uyla heyy')
speak('fatih terim')


r = sr.Recognizer()
print('Dinliyor...')
with sr.Microphone() as source:
    audio = r.listen(source)
    voice=r.recognize_google(audio,show_all=True,language='tr-TR')
    print(voice)
    

