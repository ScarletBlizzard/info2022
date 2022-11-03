import random


class TerminateConnection(Exception):
    pass

def user_connection(username):
    for i in range(random.randint(10, 20)):
        yield f"{username} message{i}" 

def write_to_file(f_obj):
    while True:
        try:
            msg = yield
            f_obj.write(msg + "\n")
        except TerminateConnection:
            f_obj.close()
            break

def connect_user(username):
    try:
        f_obj = open(f"5_messages/{username}.txt", "w", encoding="utf-8")
        write_coro = write_to_file(f_obj)
        next(write_coro)
        for msg in user_connection(username):
            write_coro.send(msg)
            yield msg
        write_coro.throw(TerminateConnection)
    finally:
        return

def establish_connection(auth, username):
    if auth:
        yield f"auth {username}"
        yield from connect_user(username)
        yield f"disconnect {username}"

def connection():
    connections = [establish_connection(True, f"User{i}") for i in range(10)]
    connections.append(establish_connection(False, "NotLoggedIn1"))
    connections.append(establish_connection(False, "NotLoggedIn2"))
    while len(connections):
        conn = random.choice(connections)
        try:
            yield next(conn)
        except StopIteration:
            del connections[connections.index(conn)]


if __name__ == "__main__":
    for i in connection():
        print(i)
