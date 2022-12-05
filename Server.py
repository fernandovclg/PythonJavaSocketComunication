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
    elif jogada == "lizard":
        return 3
    elif jogada == "spock":
        return 4
    else:
        print("ERROR")

def Decodificar(indice):
    if indice == 0:
        return "rock"
    elif indice==1:
        return "paper"
    elif indice == 2:
        return "scissors"
    elif indice == 3:
        return "lizzard"
    elif indice == 4:
        return "spock"
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
    print("knock knock penny")
    print("knock knock penny")
    print("knock knock penny")

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
    #decide sua jogada sem conhecimento do que o outro jogou
    if i==0:
        jog1 = "paper"
    else:
        max=-20000
        for j in range(0,5):
            if saldo[j]>=max:
                max=saldo[j]
                jog1=Decodificar(j)

    #armazena os resultados

    historico.append([jog1 , jog2 , Jogo(jog1,jog2)])
    if historico[i][2]=="vitoria":
        saldo[Codificar(jog1)] += 1
    elif historico[i][2]=="derrota":
        saldo[Codificar(jog1)] += 1

    #devolve a jogada decidida
    return(jog1)

historico = []
saldo =  [0,0,0,0,0]

#Main

i=0
while True :
    if i<15:
        message = clientsocket.recv(1024).decode()
        if message != "":
            jog1 = Heuristica(message,i)
            clientsocket.send((jog1+'\n').encode())

            jog2 = message
            print("resutado foi : " + Jogo(jog1 , jog2))
            i=i+1
    else:
        print("jogo finalizado")
        clientsocket.close()
        break
    

    