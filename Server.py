import socket
import threading
import dframe as df
from threading import Thread
from dframe import *
import RSACrypto as RSA

lock = threading.Lock()

def client_thread(connection):
    data = connection.recv(1024)     #receiving voter details
    #verify voter details
    log = (data.decode()).split(' ')
    log[0] = int(log[0])
    if(df.verify(log[0],log[1])):                                
        if(df.isEligible(log[0])):
            print('Voter Logged in... ID:'+str(log[0]))
            connection.send("Authenticate".encode())
        else:
            print('Vote Already Cast by ID:'+str(log[0]))
            connection.send("VoteCasted".encode())
    else:
        print('Invalid Voter')
        connection.send("InvalidVoter".encode())

    # modified start
    try:
        test = connection.recv(1024).decode()
        data, public_key = (test).split(',') #4 Get Vote

        print("Vote Received from ID: "+str(log[0])+"  Processing...")
        lock.acquire()

        #update Database                                   
        if(df.vote_update(data,log[0])):
            print("Vote Casted Sucessfully by voter ID = "+str(log[0]))
            connection.send("Successful".encode())
            public_key = RSA.base64.b64decode(public_key)
            cipher = RSA.encrypt_and_convert_to_base64(public_key, data)
            df.update_public(str(log[0]), public_key, cipher)

        else:
            print("Vote Update Failed by voter ID = "+str(log[0]))
            connection.send("Vote Update Failed".encode())
                                                                   
    # modified end

        lock.release()
    except:
        print("")
    connection.close()


def voting_Server():

    serversocket = socket.socket()
    host = socket.gethostname()
    port = 4001

    ThreadCount = 0

    try :
        serversocket.bind((host, port))
    except socket.error as e :
        print(str(e))
    print("Waiting for the connection")

    serversocket.listen(10)

    print( "Listening on " + str(host) + ":" + str(port))

    while True :
        client, address = serversocket.accept()

        print('Connected to :', address)

        client.send("Connection Established".encode())   ### 1
        t = Thread(target = client_thread,args = (client,))
        t.start()
        ThreadCount+=1
        # break

    serversocket.close()

if __name__ == '__main__':
    voting_Server()
