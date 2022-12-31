import asyncio
import rsa
from rsa import PublicKey
from protocol import read_msg, send_msg

pubkeys = dict()

async def chat(writer, reader, receiver):
    try:
        await send_msg(writer, receiver)
        if not (msg := await read_msg(reader)).endswith("offline"):
            if receiver not in pubkeys:
                pubkeys[receiver] = eval(msg)
            while True:
                msg = rsa.encrypt(input(f"{receiver} < ").encode(), pubkeys[receiver])
                await send_msg(writer, msg, False)
                await send_msg(writer, receiver)
        else:
            print(msg)
    except EOFError:
        print()
        return

async def main():
    username = input("Enter your username: ")
    reader, writer = await asyncio.open_connection(host='127.0.0.1', port=8888)
    pubkey, privkey = rsa.newkeys(512)
    await send_msg(writer, username)
    await send_msg(writer, repr(pubkey))
    try:
        while True:
            receiver = input("Chat with: ")
            await chat(writer, reader, receiver)
    except asyncio.CancelledError:
        writer.close()
        await writer.wait_closed()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print()
        print('Exiting')
