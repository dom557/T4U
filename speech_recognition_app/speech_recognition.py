# speech_recognition_app/speech_recognition.py

import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        transcription = recognizer.recognize_google(audio)
        return transcription
    except sr.UnknownValueError:
        return "Could not understand the audio"
    except sr.RequestError:
        return "Could not request results from Google Speech Recognition service"
