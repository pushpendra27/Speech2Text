import speech_recognition as speech
r=speech.Recognizer()
with speech.Microphone() as source:
    print ("Say Something Pushpendra !")
    audio=r.listen(source)
try:
    print("Google Thinks You Said:\n"+ r.recognize_google(audio))
except:
    pass
