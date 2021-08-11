from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import PIL
from PIL import ImageTk
from PIL import Image
import pyttsx3
import speech_recognition as sr

global ans
global asn2

bot = ChatBot("My Bot")
training_data_file = open('basicTraining.txt').read().splitlines() + open('acronym.txt').read().splitlines()
trainer = ListTrainer(bot)
trainer.train(training_data_file)


def Askbot():
    global ans
    if entry1.get() == "":
        messagebox.showerror("Error","Please enter the question to ask the bot")
    else:
        que = entry1.get()
        ans = bot.get_response(que.lower())

        txtBox.insert(END, "YOU :  " + que + "\n")
        txtBox.insert(END, "BOT :  " + str(ans) + "\n" + "\n")
        print("BOT :  ",str(ans))

        entry1.delete(0,END)

def Speak():
    global ans
    engine =pyttsx3.init()
    engine.say(ans)
    engine.runAndWait()

def AskToBot():
    global ans
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        audio = r.listen(source)

        ask = r.recognize_google(audio,language='eng-in')
        ask = ask.title()
        txtBox.insert(END, "YOU :  " + ask + "\n")

        ans = bot.get_response(ask.lower())
        txtBox.insert(END, "BOT :  " + str(ans) + "\n" + "\n")

root = Tk()
root.title("Main Page")
root.geometry("500x670+500+50")
root.config(bg="grey")

frame1 = Frame(root)
frame1 = LabelFrame(root, bd=8, bg='#bbded6')
frame1.place(x=10, y=10 , width=480, height=650)

img1 = Image.open("newBot.jpeg")
img1 = img1.resize((460,150), Image.ANTIALIAS)
test1 = ImageTk.PhotoImage(img1)
label1 = Label(frame1, image=test1)
label1.image = test1
label1.place(x=0,y=0)

txtBox = Text(frame1, width=44, height=16, font=('times',15))
txtBox.place(x=2,y=155)

scrlBar1 = ttk.Scrollbar(frame1, command = txtBox.yview)
scrlBar1.place(relx=1, rely=0.807, relheight=0.564, anchor='se')
txtBox.configure(yscrollcommand=scrlBar1.set)

#scrlBar2 = ttk.Scrollbar(frame1, orient='horizontal', command=txtBox.xview)
#scrlBar2.place(relx=0.49,rely=0.806,relwidth=0.97,anchor='s')
#txtBox.configure(xscrollcommand=scrlBar2.set)


label2 = Label(frame1, text="Ask Bot : ", font=("arial",15), bg='#bbded6')
label2.place(x=60,y=525)

entry1 = Entry(frame1, font=("arial",15))
entry1.place(x=160,y=525)

btn1 = Button(frame1, text="Ask Bot", font=("times",18,"bold"), fg="white", bg="#08a3d2",
            relief=RAISED, bd=5, cursor="hand2", height=1, command = Askbot)
btn1.place(x=70,y=565)

img2 = Image.open("mic.png")
img2 = img2.resize((60,40), Image.ANTIALIAS)
test2 = ImageTk.PhotoImage(img2)
label3 = Label(frame1, image=test2, bg='#bbded6')
label3.image=test2

btn2 = Button(frame1, image=test2, cursor="hand2", bg='#bbded6', relief=RAISED, bd=5, compound=LEFT, command=Speak)
btn2.place(x=220,y=565)

img3 = Image.open("speak.png")
img3 = img3.resize((60,40), Image.ANTIALIAS)
test3 = ImageTk.PhotoImage(img3)
label4 = Label(frame1, image=test3, bg='#bbded6')
label4.image=test3

btn3 = Button(frame1, image=test3, cursor="hand2", bg='#bbded6', relief=RAISED, bd=5, compound=LEFT, command=AskToBot)
btn3.place(x=320,y=565)


root.mainloop()
