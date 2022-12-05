#Imports Modules
import socket
# from array import *

#Defines Server Values
listensocket = socket.socket()
Port = 8000
maxConnections = 999
IP = socket.gethostname() #Gets Hostname Of Current Macheine

listensocket.bind(('',Port))

#Opens Server
listensocket.listen(maxConnections)
print("Server started at " + IP + " on port " + str(Port))

#Accepts Incomming Connection
(clientsocket, address) = listensocket.accept()
print("New connection made!")

running = True

#funções auxiliares

def Codificar(jogada):
    if jogada == "rock":
        return 0
    elif jogada=="paper":
        return 1
    elif jogada == "scissors":
        return 2
    elif jogada == "lizzard":
        return 3
    elif jogada == "spock":
        return 4
    else:
        print("ERROR")

def Jogo (jog1,jog2):

    M=[[ 0,-1, 1, 1,-1],
       [ 1, 0,-1,-1, 1],
       [-1, 1, 0, 1,-1],
       [-1, 1,-1, 0, 1],
       [ 1,-1, 1,-1, 0]]
    if M[Codificar(jog1)][Codificar(jog2)]==1 :
        return("vitoria")
    elif M[Codificar(jog1)][Codificar(jog2)]==0 :
        return("empate")
    elif M[Codificar(jog1)][Codificar(jog2)]==-1 :
        return("derrota")
  
def Menu():
    print("Jogadas Permitidas:\n" +
                    "rock\n" +
                    "paper\n" +
                    "scissors\n" +
                    "lizard\n" +
                    "spock\n")
    print("digite sua jogada: ")
    jog1='paper'
    # jog1 = input()
    return(jog1)
def Heuristica(jog2,i):
    if i==0:
        jog1 = "paper"
    else:
        jog1=historico[0][0]

    historico.append([jog1 , jog2 , Jogo(jog1,jog2)])
    return(jog1)

historico = []

#Main

i=0
while True :
    message = clientsocket.recv(1024).decode()
    if message != "":
        jog1 = Heuristica(message,i)
        clientsocket.send((jog1+'\n').encode())

        jog2 = message
        print("resutado foi : " + Jogo(jog1 , jog2))
        i=i+1
    # else:
        # print("nao")
clientsocket.close()
    

    