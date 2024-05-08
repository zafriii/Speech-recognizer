import speech_recognition as sr
import os

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  
        audio = recognizer.listen(source) 

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)

        if "Run my website" in command:
            project_directory_frontend = "D:/MERN app/frontend"
                    
            os.chdir(project_directory_frontend)
           
            os.system("npm run dev")
         

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

if __name__ == "__main__":
    recognize_speech()
