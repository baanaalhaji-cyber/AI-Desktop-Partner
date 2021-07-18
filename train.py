def say(val):
        # pip install pyttsx3 pypiwin32
    import pyttsx3

    # One time initialization
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')

    # Set properties _before_ you add things to say
    engine.setProperty('rate', 120)    # Speed percent (can go over 100)
    engine.setProperty('volume', 1.0)  # Volume 0-1
    #engine.setProperty('voice', voices[11].id)

    # Queue up things to say.
    # There will be a short break between each one
    # when spoken, like a pause between sentences.
    engine.say(val)
    
    # Flush the say() queue and play the audio
    engine.runAndWait()

    # Program will not continue execution until
    # all speech is done talking

def name_identifier(S):
    temp = []
    S = S.split()

    for i in S:
        if i == 'your' or i == 'name':
            temp.append(i)
    
    if len(temp) < 1:
        return False

    if temp[0] == 'your':
        return True
    return False 

#print(name_identifier("your name"))
#say("Hello World!!!")
