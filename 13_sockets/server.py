import sys
import socket
import selectors
import types

sel = selectors.DefaultSelector()

host, port = sys.argv[1], int(sys.argv[2])
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen()
print(f"Listening on {(host, port)}")
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)

users = {}
MSG_DELIMITER = b'<'
ENCODING = 'ascii'

def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print(f"Accepted connection from {addr}")
    conn.setblocking(False)
    data = types.SimpleNamespace(known=False, username=b'', msg=b'')
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)


def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)
        if recv_data:
            if not data.known:
                username = recv_data.decode(ENCODING)
                users[username] = key
                data.username = username
                data.known = True
            else:
                if recv_data == b'list':
                    data.msg = b"Users online: " + ', '.join(users.keys()).encode(ENCODING)
                elif MSG_DELIMITER in recv_data:
                    recipient, msg = recv_data.split(MSG_DELIMITER, 1)
                    recipient = recipient.decode(ENCODING)
                    if recipient in users:
                        users[recipient].data.msg = data.username.encode(ENCODING) + b': ' + msg
        else:
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.msg:
            sent = sock.send(data.msg)
            data.msg = data.msg[sent:]


try:
    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                service_connection(key, mask)
except KeyboardInterrupt:
    print("Caught keyboard interrupt, exiting")
finally:
    sel.close()
