import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')

engine.setProperty('voice' , voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def takeCommand():
    global query
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Next ball comming up")
        print ('What happend on this ball : ')
        r.pause_threshold = 1
        r.energy_threshold = 200
        audio = r.listen(source)
    try:
        data='something'
        data= r.recognize_google(audio,language='en-US')
        query = str(data)

    except sr.UnknownValueError:
        print ('Attention ! Google could not understand audio')
        data='Could not understand anything'
    except sr.RequestError as e:

       print ('Attention ! Could not request results from Google service.')

    print("User said : ",data)
    
if __name__ == "__main__":

    import mysql.connector as conn

    con = conn.connect(host = "localhost" , user = "root" , password = "" , database = "crickpoint")
    cur = con.cursor()
    if con.is_connected():
        print("Established")
    else :
        print("Failed")
    while True :
           
            
            for j in range(2):
                x = "Create table over{} (Ball integer , Runs integer , Commentary Varchar(100));".format(j+1)
                
                cur.execute(x)
                con.commit()
                global y
                global query
                global z
                l= []
                for i in range(2):
                    
                    y= int(input("What happened on this ball : "))
                    print("Ball",i+1,": ",y)
                    z = l.append(y)
                    takeCommand()
                    print("Ball",i+1,": ",query)
                    cur = con.cursor()
                    cur.execute("Insert into over{} values ({}, {}, '{}')".format(j+1,i+1,y,query))
                    
                print("Total runs for the over : " ,  sum(l))
                   
            break                           
            
