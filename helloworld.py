import socket

def get_Host_name():
    try:
        host_name = socket.gethostname()
        print("You did it. Welcome to hello world of",host_name)
    except:
        print("Unable to get Hostname")
 
# Driver code
get_Host_name() #Function call