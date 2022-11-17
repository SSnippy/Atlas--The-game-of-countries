#importing modules 
import speech_recognition as sr 
import random 
import pyttsx3 
import os 
import time
import cv2



letterchangedlist=[]

engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
  
#defining functions 
def speakm(audio): 
    engine.setProperty('voice', voices[0].id) 
    engine.say(audio) 
    engine.runAndWait()
    engine.setProperty("rate",180)
 
def speakf(audio): 
    engine.setProperty('voice', voices[1].id) 
    engine.say(audio) 
    engine.runAndWait()
    engine.setProperty("rate",180)


 
def listcheck(lis):
    lisaa=globals()[lis]
    l=len(lisaa)    
    if l==0:
        countrylist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        letindex=countrylist.index(lis)
        if letindex==25:
            listcheck("a")
        elif letindex!=25:
            xaa=chr(ord(lis)+1)
            listcheck(xaa)
    else:
        print(lis)
        letterchangedlist.clear()
        letterchangedlist.append(lis)



  
def setup(country,listof): 
    let.clear() 
    lastlet=country[-1] 
    let.append(lastlet) 
    listof.remove(country) 
  
#UI 
print("*****RULES*****\n1)The player gets one chance to give a country before the computer goes\n2)This is a country only atlas\n3)No inappropriate input(i.e United states of america cant be given as america)\n4)Normal altlas rules apply.\n5) to stop playing say \"i want to stop playing\"") 
print("-------------------------------------------------------------------------------------------------------------------------------------------")                                                                                    #female 
name=input("Enter Username: ") 
usercallout="alright",name,"let's play" 
speakf(usercallout) 
speakf(''' 
You go first 
The letter is S''')                                                          #female  
  
#countries 
a=["afghanistan","albania","algeria","andorra","angola","antigua and barbuda","argentina","armenia","australia","austria","azerbaijan","africa"] 
b=["bahamas","bahrain","bangladesh","barbados","belarus","belgium","belize","benin","bhutan","bolivia","bosnia and herzegovina","botswana","brazil","brunei","bulgaria","burkina faso","burundi"] 
c=["cabo verde","cambodia","cameroon","canada","cayman islands","cantral african republic","chad","chile","china","colombia","comoros","costa rico","croatia","cuba","cyprus","czechia","czechoslovakia"] 
d=["democratic republic of congo","denmark","djibouti","dominician republic","duchy of parma"] 
e=["ecudor","egypt","el salvador","eritrea","estonia","eswatini","ethiopia"] 
f=["fiji","finland","france"] 
g=["gabon","gambia","georgia","germany","ghana","greece","grenada","guatemala","guinea"] 
h=["hanover","hanseatic republics","hawaii","hesse","holy see","honduras","hungary","haiti"] 
i=["iceland","india","indonesia","iran","iraq","ireland","isreal","italy"] 
j=["jamaica","japan","jordan"] 
k=["kazakhstan","kenya","kingdom of serbia","kiribati","korea","kosovo","kuwait","kyrgyzstan"] 
l=["loas","latvia","lebanon","lesotho","lew chew","liberia","libya","liechtenstein","lithuania","luxembourg"] 
m=["madagascar","malawi","malaysia","maldives","mali","malta","marshall islands","mauritania","mauritius","mecklenburg schwerin","mexico","micronesia","moldova","monaco","mongolia","montenegro","morocco","mozambiqe"] 
n=["nambia nassau","nauru","nepal","netherlands","new zealand","nicaragua","nigeria","north macedonia","norway","north korea"] 
o=["oldenburg","oman"] 
p=["pakistan","palau","papua new guinea","paraguay","peru","philippines","poland","portugal"] 
q=["qatar"] 
r=["republic of genoa","romonia","russia","rwanda"]
s=["south korea","saint kitts and nevis","saint luia","samoa","san marino","saudi arabia","senegal","serbia","sierra leone","singapore","slovakia","slovenia","solomon island","somalia","south africa","south sudan","spain","sri lanka","sudan","suriname","sweden","switzeland","syria"] 
t=["tajikistan","tanzania","thailand","togo","tonga","trinidad and tobago","the united states of america","tunisia","turkey","turmekistan","tuvalu"] 
u=["uganda","ukraine","united arab emirates","united kingdom","uruguay","uzbekistan"] 
v=["vanuatu","venezuela","vietnam","wurttemberg"] 
w=[] 
x=[] 
y=["yemen"] 
z=["zambia","zimbawe","zabol","zagazig","zanzibar"] 
  
mytime=0 
score=0 
  
#loop starts 
let=["s"] 
ind1=0 
start=time.time() 
 
while ind1<98: 
      
    #player list check function 
    checkletter=let[0] 
    listcheck(checkletter) 
    letchanged=letterchangedlist[0]
    if letchanged!=let[0]:
        let.clear()
        let.append(letchanged) 
        tobespoken="the letter has been changed, the new letter is: ",letchanged
        speakf(tobespoken)
        print("the letter has been changed, the new letter is: ",letchanged) 

         
    #mic config
    
    country=""
    while country=="":
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("listening")
            ro = sr.Recognizer()
            with sr.Microphone() as source:
                global audio
                audio = ro.listen(source)
            countryp =ro.recognize_google(audio) 
            countryp1=str(countryp) 
            country=countryp1.casefold()
    print(country) 
    
    #players turn 
    if country!="i want to stop playing": 
        if country[0]==let[0]: 
            globalcountry=let[0] 
            glovar=globals()[globalcountry] 
            if country in glovar: 
                print("accpeted") 
                setup(country,glovar) 
                     
                #computers list check function 
                checkletter2=let[0] 
                listcheck(checkletter2)
                letchanged2=letterchangedlist[0]
                if letchanged2!=let[0]:
                    let.clear()
                    let.append(letchanged2) 
                    tobespoken2="the letter has been changed, the new letter is: ",letchanged2
                    speakf(tobespoken2)
                    print("the letter has been changed, the new letter is: ",letchanged2)  

                score=score+1 
     
                #computers turn starts 
                globalcountry1=let[0] 
                glovar1=globals()[globalcountry1] 
                lenofcon=len(glovar1)-1 
                randomcon=random.randint(0,lenofcon) 
                computercountry=glovar1[randomcon] 
                         
                print("computer choose: ",computercountry) 
                speakm(computercountry)                                                      #male 
                print("your letter is: ",computercountry[-1]) 
                setup(computercountry,glovar1) 
            else: 
                speakf("country doesnt exist or already used") 
                mytime=mytime-3 
        else: 
            speakf("wrong letter try again") 
            mytime=mytime-3 
  
    end=time.time() 
    timethisround=end-start 
    mytime=mytime+timethisround 
    #stop playing  
    if country=="i want to stop playing": 
        speakf("thank you for playing")                                #female 
        if mytime>=6: 
             mytime=mytime-5 
        print("\n") 
        namec=name.casefold() 
        print("player: ",namec,"had a score of: ",score,"in time: ",mytime) 
        os._exit(1) 
    ind1=ind1+1 
  
print("\n") 
namec=name.casefold() 
print("player: ",namec,"had a score of: ",score,"in time: ",mytime) 
endgame="no more contries left, well played. the game has ended. thank you for playing" 
print("GameEnd. Thank you for playing") 
speakf(endgame)                                                          #female 
os._exit(1)
 
