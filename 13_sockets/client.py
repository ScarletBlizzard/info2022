import sys
import socket
import selectors
from threading import Thread
from time import sleep
import types


def print_help():
    print()
    print("Help: ")
    print("Type %username%<%msg% to send a" + \
          " message %msg% to user named %username%")
    print("Type 'stop' to exit")
    print("Type 'list' to get list of users online")
    print("Type 'help' for help")
    print()


sel = selectors.DefaultSelector()
ENCODING = 'ascii'

class KeyboardThread(Thread):

    def __init__(self):
        self.input = []
        self.stop = False
        super().__init__()

    def run(self):
        print_help()
        print("Enter your name:")
        while True:
            if self.stop:
                break
            self.input.append(input())


def start_connection(sel, host, port):
    server_addr = (host, port)
    print(f"Starting connection to {server_addr}")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.connect_ex(server_addr)
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    data = types.SimpleNamespace(
        outb=b"",
    )
    sel.register(sock, events, data=data)

if __name__ == '__main__':
    host, port = sys.argv[1], int(sys.argv[2])
    sel = selectors.DefaultSelector()
    start_connection(sel, host, port)
    kthread = KeyboardThread()
    kthread.start()
    while(True):
        events = sel.select(timeout=None)
        for key, mask in events:       
            sock = key.fileobj
            data = key.data
            if mask & selectors.EVENT_READ:
                recv_data = sock.recv(1024)  # Should be ready to read
                if recv_data:
                    print(recv_data.decode(ENCODING))
            if mask & selectors.EVENT_WRITE:
                if not data.outb and kthread.input:
                    input_text = kthread.input.pop()
                    if input_text == 'stop':
                        kthread.stop = True
                        sel.unregister(sock)
                        sock.close()
                        exit(0)
                    elif input_text == 'help':
                        print_help()
                    else:            
                        data.outb = input_text.encode(ENCODING)
                if data.outb:
                    sent = sock.send(data.outb)  # Should be ready to write
                    data.outb = data.outb[sent:]             
