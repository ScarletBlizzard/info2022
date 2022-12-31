import asyncio
import rsa
from protocol import read_msg, send_msg

async def main():
    username = input("Enter your username: ")
    reader, writer = await asyncio.open_connection(host='127.0.0.1', port=8888)
    pubkey, privkey = rsa.newkeys(512)
    await send_msg(writer, username)
    await send_msg(writer, repr(pubkey))
    try:
        while msg := await read_msg(reader, False):
            print(rsa.decrypt(msg, privkey).decode())
        print('Connection ended.')
    except asyncio.IncompleteReadError:
        print('Server closed.')
    finally:
        writer.close()
        await writer.wait_closed()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bye!')
