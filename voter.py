import tkinter as tk
import socket
from tkinter import *
from VotingPage import votingPg
import RSACrypto as RSA
import dframe as df

def establish_connection():
    host = socket.gethostname()
    port = 4001
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(client_socket)
    message = client_socket.recv(1024)      #connection establishment message   #1
    if(message.decode()=="Connection Established"):
        return client_socket
    else:
        return 'Failed'


def view_vote(frame1, private_key, voter_id):
    try:
        Label(frame1, text="Vote:  " + RSA.decrypt_message(RSA.base64.b64decode(private_key), RSA.base64.b64decode(df.get_ciper(voter_id))), anchor="e", justify=LEFT).grid(row = 5,column = 0)
    except:
        Label(frame1, text="Your private key is incorrect", anchor="e", justify=LEFT).grid(row = 5,column = 0)
        
def failed_return(root,frame1,client_socket,message, voter_id = '10001'):
    for widget in frame1.winfo_children():
        widget.destroy()
        
    Label(frame1, text=message, font=('Helvetica', 12, 'bold')).grid(row = 1, column = 0, columnspan = 2, padx=120, pady=10)

    # start modified

    if message == "Vote has already been cast":
        Label(frame1, text="To check your voting,\nplease enter your private key:").grid(row = 3,column = 0, sticky=W+E)
        private_key = tk.StringVar()
        e2 = Entry(frame1, textvariable = private_key, width=30).grid(row = 3, column = 1, sticky=W)
        sub = Button(frame1, text="view", width=10, command = lambda: view_vote(frame1, private_key.get(), voter_id))
        sub.grid(row = 4, column = 0, columnspan = 2, pady=10)

    # end modified

    client_socket.close()

def log_server(root,frame1,client_socket,voter_ID,password):
    message = voter_ID + " " + password
    client_socket.send(message.encode()) #2

    message = client_socket.recv(1024) #Authenticatication message
    message = message.decode()

    if(message=="Authenticate"):
        votingPg(root, frame1, client_socket)

    elif(message=="VoteCasted"):
        message = "Vote has already been cast"
        failed_return(root,frame1,client_socket,message,voter_ID)

    elif(message=="InvalidVoter"):
        message = "Invalid Voter"
        failed_return(root,frame1,client_socket,message)

    else:
        message = "Server Error"
        failed_return(root,frame1,client_socket,message)



def voterLogin(root,frame1):

    client_socket = establish_connection()
    if(client_socket == 'Failed'):
        message = "Connection failed"
        failed_return(root,frame1,client_socket,message)

    root.title("Voter Login")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Voter Login", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 2, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)
    Label(frame1, text="Voter ID:      ", anchor="e", justify=LEFT).grid(row = 2,column = 0)
    Label(frame1, text="Password:   ", anchor="e", justify=LEFT).grid(row = 3,column = 0)

    voter_ID = tk.StringVar()
    name = tk.StringVar()
    password = tk.StringVar()

    e1 = Entry(frame1, textvariable = voter_ID)
    e1.grid(row = 2,column = 2)
    e3 = Entry(frame1, textvariable = password, show = '*')
    e3.grid(row = 3,column = 2)

    sub = Button(frame1, text="Login", width=10, command = lambda: log_server(root, frame1, client_socket, voter_ID.get(), password.get()))
    Label(frame1, text="").grid(row = 4,column = 0)
    sub.grid(row = 5, column = 3, columnspan = 2)

    frame1.pack()
    root.mainloop()


# if __name__ == "__main__":
#         root = Tk()
#         root.geometry('500x500')
#         frame1 = Frame(root)
#         voterLogin(root,frame1)
