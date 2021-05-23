#!/usr/bin/python

# Import socket module
import socket
def Main():
    # local host IP '127.0.0.1 '
    host = '127.0.0.1'
    # Definition des Ports, an dem Sie eine Verbindung herstellen
    port = 1000
    # Verbindung zum Server auf dem lokalen Computer
    s = socket.socket(socket.AF_INET ,socket.SOCK_STREAM) #Socket Connection
    s.connect((host,port))
    # vom Server empfangene Nachricht

    List=[] #informationen von Studenten werden in einem List gespeichert.
    
    List.append(raw_input("Der Name des Students : ")) #Weil wir benutzen Python 1, braucht man rawinput um eingaben in das List einzugeben. Andererfalls gibt es Fehler.
    List.append(raw_input("Die Matrikelnummer des Students : "))
    List.append(raw_input("Die Note des Students : "))

    s.send(str(List).encode()) #Senden von List in einer String format, weil send funktion nur String variablen annimmt.
    data = s.recv(1024).decode() #Empfangen von Data durch Socket wieder durch recv funktion. 1024 ist Baudrate.

    
    # Ausschliesen der Anschluss
    s.close()


if __name__ == '__main__':
    i = "j"
    while i=="j": # To take multiple inputs, i have created an iteration here
        Main ()
        i = raw_input("Moechten Sie weiterhin Die Studentdaten erhalten? (j / n) ")