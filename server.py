#!/usr/bin/python
import socket
from thread import *
import threading 
import sys
#Geben Sie die Informationen ueber die Studenten
name_list = []
number_list = [] 
grade_list = []
print_lock = threading.Lock()
# thread function
def threaded(c):
   
    while True:
        # Recieving the data from client with recv function. 1024 is the baudrate
        data = c.recv(1024)
        lenName = len(name_list)
        if not data:
            sys.stdout.flush()
            # lock released on exit
            print_lock.release()
            break
        else:
            vdata = data #Temporary variable for recieved data. I set it this way because program flushes the data in this string when iterating for 2nd time.
            xList = vdata.strip('][').split(', ') #This function i found from the StackOverFlow. We want to transform the received String to a List again so that we can add the elements to categories.
            
            name_list.append(xList[0]) #Adding received Name to server name list
            number_list.append(xList[1])#Adding received Number to server number list
            grade_list.append(xList[2])#Adding received Grade to server grade list

            print(str(name_list[lenName]) + " " + "wurde zur Datenbank addiert.\n") #Confirming that these process is complete (added for test purposes)
      
        print("Student" + " "+ str(lenName+1) + ":" +name_list[lenName] + " " + number_list[lenName] + " " + grade_list[lenName]) #This line is what we see when we check server status
        # Sendung die Daten an den Client
        c.send(data.encode()) 
   
    # Verbindung ist geschlossen
    c.close()
def Main(): 
    host = ""
    port = 1000
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM) 
    s.bind((host, port))
    s.listen(5)
    while True:
        # Verbindung mit dem Client herstellen
        c, addr = s.accept()
        print_lock.acquire()
        sys.stdout.flush()
        start_new_thread(threaded , (c,)) 
    s.close()
    
if __name__ == '__main__':
    Main ()