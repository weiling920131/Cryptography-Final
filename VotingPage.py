import tkinter as tk
import socket
from tkinter import *
from PIL import ImageTk,Image
import RSACrypto as RSA

def voteCast(root,frame1,vote,client_socket):
    for widget in frame1.winfo_children():
        widget.destroy()

    # start modified 
    
    private_key, public_key = RSA.generate_rsa_key_pair()
    votekey = vote + ',' + RSA.convert_to_base64(public_key)
    client_socket.send(votekey.encode()) #4
    print(f"Your private key: {RSA.convert_to_base64(private_key)}")

    # end modified 

    message = client_socket.recv(1024) #Success message
    message = message.decode()
    if(message=="Successful"):
        Label(frame1, text="Vote Casted Successfully", font=('Helvetica', 18, 'bold')).grid(row = 1, column = 1)
        
    else:
        Label(frame1, text="Vote Cast Failed... \nTry again", font=('Helvetica', 18, 'bold')).grid(row = 1, column = 1)

    client_socket.close()



def votingPg(root,frame1,client_socket):

    root.title("Cast Vote")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Cast Vote", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)

    vote = StringVar(frame1,"-1")

    Radiobutton(frame1, text = "whp1230\n\n資工14系排大砲", variable = vote, value = "whp1230", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"whp1230",client_socket)).grid(row = 2,column = 1)
    bjpLogo = ImageTk.PhotoImage((Image.open("img/0.png")).resize((70,70),Image.ANTIALIAS))
    bjpImg = Label(frame1, image=bjpLogo).grid(row = 2,column = 0)

    Radiobutton(frame1, text = "jox__sid\n\nGPE戰神", variable = vote, value = "jox__sid", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"jox__sid",client_socket)).grid(row = 3,column = 1)
    congLogo = ImageTk.PhotoImage((Image.open("img/1.png")).resize((70,70),Image.ANTIALIAS))
    congImg = Label(frame1, image=congLogo).grid(row = 3,column = 0)

    Radiobutton(frame1, text = "r14.07p\n\n大推網通原", variable = vote, value = "r14.07p", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"r14.07p",client_socket) ).grid(row = 4,column = 1)
    aapLogo = ImageTk.PhotoImage((Image.open("img/2.png")).resize((70,70),Image.ANTIALIAS))
    aapImg = Label(frame1, image=aapLogo).grid(row = 4,column = 0)

    Radiobutton(frame1, text = "weiling_0131\n\n頭髮 會長 出來啦", variable = vote, value = "weiling_0131", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"weiling_0131",client_socket)).grid(row = 5,column = 1)
    ssLogo = ImageTk.PhotoImage((Image.open("img/3.png")).resize((70,70),Image.ANTIALIAS))
    ssImg = Label(frame1, image=ssLogo).grid(row = 5,column = 0)

    Radiobutton(frame1, text = "rueixsun\n\n6/16來看熱舞大成", variable = vote, value = "rueixsun", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"rueixsun",client_socket)).grid(row = 6,column = 1)
    notaLogo = ImageTk.PhotoImage((Image.open("img/4.png")).resize((70,70),Image.ANTIALIAS))
    notaImg = Label(frame1, image=notaLogo).grid(row = 6,column = 0)

    frame1.pack()
    root.mainloop()

