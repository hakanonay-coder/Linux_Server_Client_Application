#!/usr/bin/python

# Import socket module
import socket
def Main():
    # local host IP '127.0.0.1 '
    host = '127.0.0.1'
    # Definition des Ports, an dem Sie eine Verbindung herstellen
    port = 1000
    # Verbindung zum Server auf dem lokalen Computer
    s = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
    s.connect((host,port))
    # vom Server empfangene Nachricht

    inpList=[]
    
    inpList.append(raw_input("Der Name des Students : "))
    inpList.append(raw_input("Die Matrikelnummer des Students : "))
    inpList.append(raw_input("Die Note des Students : "))

    s.send(str(inpList).encode())
    data = s.recv(1024).decode()

    #!!Bis hierher!!
    # close the connection
    s.close()
if __name__ == '__main__':
    i = "j"
    while i=="j":
        Main ()
        i = raw_input("Moechten Sie weiterhin Die Studentdaten erhalten? (j / n) ")