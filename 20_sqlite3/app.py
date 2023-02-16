import sqlite3

help_str = """
Available commands:
books   - List books
readers - List readers
book    - Add book
reader  - Add reader
give    - Give book to reader
take    - Take book from reader
exit    - Exit app
""" 

def fetch_ids(conn, name, author, title):
    return (
    conn
        .execute('select id from Readers where name = ?', (name,))
        .fetchone()[0],
    conn
        .execute('select id from Books where title = ? AND author = ?',
            (title, author))
        .fetchone()[0]
    )

if __name__ == "__main__":
    conn = sqlite3.connect("data.db")
    #conn.row_factory = sqlite3.Row
    while True:
        cmd = input("> ").lower()
        if cmd == "books":
            with conn:
                for row in conn.execute('select * from Books'):
                    print(row)
        elif cmd == "readers":
            with conn:
                for row in conn.execute('select * from Readers'):
                    print(row)
        elif cmd == "book":
            author = input("> Author: ")
            title = input("> Title: ")
            publish_year = int(input("> Publish year: "))
            with conn:
                conn.execute('insert into Books(author, title, publish_year) values (?, ?, ?)', (author, title, publish_year))
                print("OK")
        elif cmd == "reader":
            name = input("> Name: ")
            with conn:
                conn.execute('insert into Readers(name) values (?)', (name,))
                print("OK")
        elif cmd == "give":
            name = input("> To: ")
            author = input("> Book author: ")
            title = input("> Book title: ")
            with conn:
                reader_id, book_id = fetch_ids(conn, name, author, title)
                conn.execute('insert into Records(reader_id, book_id, taking_date) values (?, ?, datetime("now", "localtime"))', (reader_id, book_id))
                print("OK")
            pass
        elif cmd == "take":
            name = input("> From: ")
            author = input("> Book author: ")
            title = input("> Book title: ")
            with conn:
                reader_id, book_id = fetch_ids(conn, name, author, title)
                conn.execute('update Records set returning_date = datetime("now", "localtime") where reader_id = ? AND book_id = ?', (reader_id, book_id))
                print("OK")
        elif cmd == "exit":
            break
        else:
            print(help_str)
