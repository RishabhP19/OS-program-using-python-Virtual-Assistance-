import pyttsx3
import os
import datetime
import random
import webbrowser
import wikipedia
import calendar

now = datetime.datetime.now()
hour = now.hour
engine = pyttsx3.init()
engine.setProperty('rate',175)



if hour < 12:
    engine.say("Hey, Good morning  It's nice to meet you . My name is Alita")
    engine.runAndWait()
    
elif hour < 18:
    engine.say("Hey, Good afternoon  It's nice to meet you . My name is Alita")
    engine.runAndWait()
    
else:
    engine.say("Hey, Good night  It's nice to meet you . My name is Alita")
    engine.runAndWait()
    
print("*"*80,"\n","~"*80,'\n\n\t\t\tWelcome. My name is Alita','\n'," "*56,"(Press --help for menu)","\n",'~'*80,"\n",'*'*80)
engine.say("What\'s your name Buddy?'")
engine.runAndWait()
print ("What\'s your name , Buddy?' : ",end='')
name=input()    

print ('Hello %s, what can i do for u mate?  : '%(name),end='')

engine.say("what can i do for u"+name)
engine.runAndWait()
    
while True:
    q=input()
    p=q.lower()
    print('\n',"\n",'~'*80,"\n",'*'*80)
    
    if ((("how" in p) and ("help" in p)) or (('what' in p) and ('options'))) or ('--help' in p):
        print(' ~ I can run chrome browser for you and browse any site you like \n ~ I Can tell you about anything you want , just type these magical words "TELL ME ABOUT" \n ~ Can show you Calendar \n ~ Wikipedia search \n ~ Can shutdown your pc \n ~ Can restart your pc \n ~ Can open notepad \n ~ Can tell you current date & time \n ~ Can open VLC player  ')
        print('What else i can do for you? : ',end='')
        engine.say("What else i can do for you?")
        engine.runAndWait()
        

    
    elif ((('run' in p) or ("open" in p)) and ('chrome' in p)) or ("website" in p):
        print('Which website do you want to browse on chrome? \n (eg. Facebook.com,Google.com,Wikipedia.org) :',end='')
        engine.say("Which website do you want to browse on chrome?")
        engine.runAndWait()
        domain=input()
        url = 'https://www.'+domain
        webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
        webbrowser.get('chrome').open(url)
        print('What else i can do for you? : ',end=' ')
        engine.say("What else i can do for you?")
        engine.runAndWait()
       
    
    
    elif ("wikipedia" in p) or ('tell me about' in p):
        engine.say("What do you wanna know about?")
        engine.runAndWait()
        print("What do you wanna know about? \n (eg. India,Taj Mahal,Sun,etc.) : ",end='')
        name2=input()
        name2= name2.replace("wikipedia", "")
        result = wikipedia.summary(name2, sentences=3)
        print(result)
        print ('Do you want to know more about this topic? \n (y/n) : ',end='')
        answers=input()
        if answers=="y":
            name2= name2.replace("wikipedia", "")
            result = wikipedia.summary(name2, sentences=6)
            print(result)
        print('What else i can do for you? : ',end='')
        engine.say("What else i can do for you?")
        engine.runAndWait()
    
    elif ("calendar" in p) :
        engine.say("Please enter year")
        engine.runAndWait()
        year = int(input("Please enter year: "))
        engine.say("please enter month")
        engine.runAndWait()
        month = int(input("Please enter month: "))
        print(calendar.month(year, month))
        print('What else i can do for you? : ',end='')
        engine.say("What else i can do for you?")
        engine.runAndWait()
        
    
    elif ("shutdown" in p):
        engine.say("Are you sure, you want to shutdown your computer ?")
        engine.runAndWait()
        shutdown = input("Want to shutdown your computer ? (y/n): ");
        if shutdown == 'y':
            os.system("shutdown /s /t 1")
        else:
            print('What else i can do for you? : ',end='')
            engine.say("What else i can do for you?")
            engine.runAndWait()
    
    elif ("restart" in p):
        engine.say("Are you sure, you want to restart your computer ?")
        engine.runAndWait()
        restart = input("Want to shutdown your computer ? (y/n): ");
        if restart == 'y':
            os.system("shutdown /r /t 1");
        else:
            print('What else i can do for you? : ',end='')
            engine.say("What else i can do for you?")
            engine.runAndWait()
    
    elif ("hi" in p) or ("hello" in p) or ( 'hola' in p) or ("wassup" in p):
        output=['howdy','what\'s good', 'hello','hi there']
        print(random.choice(output))
        print('what can i do for u buddy? : ',end='')
        engine.say("what can i do for u buddy?")
        engine.runAndWait()
      
    
    
    elif (('run' in p) or ('execute' in p) or ("open" in p)) and (("notepad" in p) or ('editor' in p)) :
        os.system('notepad')
        print('What else i can do for you? : ',end='')
        engine.say("What else i can do for you?")
        engine.runAndWait()
       
        
   

    elif ("run" in p) and ('vlc' in p) :
        os.system('vlc') 
        print('What else i can do for you? : ',date,end='')
        engine.say("What else i can do for you?")
        engine.runAndWait()
       
    
    elif ("date" in p) or ("time" in p):
        print('Today\'s date & current time is : ',end='')
        engine.say("Today\'s date & current time is") 
        engine.runAndWait()
        print(now)
        engine.say(now)
        engine.runAndWait()
        print('What else i can do for you? : ',end='')
        engine.say("What else i can do for you?") 
        engine.runAndWait()
       
    
        
    elif ('exit' in p) or ('quit' in p) :
        print('Are you sure you want to leave? :( \n (y/n) : ',end="")
        engine.say("Are you sure you want to leave?") 
        engine.runAndWait()
        ans=input()
        if ans== "y" :
            goodbuy=[' I don\'t like goodbyes so let\'s just say see you soon :)','Happiness is knowing I an going to see you soon :)','I get to see you ...soon..:)',
                 'I can\'t wait to see you soon :) ','See you soon :)']
            print(random.choice(goodbuy))  
            break 
            
        print('What else i can do for you? : ',end=' ')
        engine.say("What else i can do for you?")
        engine.runAndWait()
            
    
    else :
        errors=['I don\'t know what you mean','Excuse me?','OOPS!! I can\'t find it','Sorry it dosen\'t exist','I can\'t get you everything , LOL!!😁']
        print(random.choice(errors))
        print('What else i can do for you? : ',end=' ')
        engine.say("What else i can do for you?")
        engine.runAndWait()
       
