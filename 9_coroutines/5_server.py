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
    f_obj = open(f"5_messages/{username}.txt", "w", encoding="utf-8")
    write_coro = write_to_file(f_obj)
    yield from write_coro 

def establish_connection(auth, username):
    if auth:
        yield f"auth {username}"
    yield from user_connection(username)
    if auth:
        yield f"disconnect {username}"

def connection():
    connections = [establish_connection(True, f"User{i}") for i in range(10)]
    connections.extend([establish_connection(False, f"NotLoggedIn{i}") for i in range(2)])
    while len(connections):
        conn = random.choice(connections)
        try:
            yield next(conn)
        except StopIteration:
            del connections[connections.index(conn)]

def main():
    logged_users_coros = {}
    for conn in connection():
        msg = conn.split()
        if msg[0] == "auth":
            username = msg[1]
            logged_users_coros[username] = connect_user(username)
            next(logged_users_coros[username])
        elif msg[0] == "disconnect":
            username = msg[1]
            if username in logged_users_coros:
                try:
                    logged_users_coros[username].throw(TerminateConnection)
                finally:
                    del logged_users_coros[username]
                    continue
        else:
            username = msg[0]
            if username in logged_users_coros:
                logged_users_coros[username].send(msg[1])


if __name__ == "__main__":
    main()
