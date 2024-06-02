import speech_recognition as sr
from playsound import playsound

def listen_and_transcribe():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Starting...")
        playsound('start.wav')   
        print("Hello Sir 😊")

        while True:
            try:   
                print("you can talk ...")
                audio = recognizer.listen(source, timeout=5)
                transcription = recognizer.recognize_google(audio)
                if  "off"  in transcription:
                    print("Turnning off the systeme ... ")
                    print("Bye sir 😊")
                    break
                print("You said: " + transcription)
            except sr.WaitTimeoutError:
                continue
            except sr.UnknownValueError:
                print("Could not understand the audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    listen_and_transcribe()
