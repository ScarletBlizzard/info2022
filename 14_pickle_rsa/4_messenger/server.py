import asyncio
from protocol import read_msg, send_msg

receivers = dict()
pubkeys = dict()
friends = dict()

async def handle_connection(reader, writer):
    peername = writer.get_extra_info('peername')
    username = await read_msg(reader)
    pubkey = await read_msg(reader)
    receivers[username] = writer
    pubkeys[username] = pubkey
    friends[username] = set()
    print(f'Remote {peername} connected')
    try:
        while receiver := await read_msg(reader):
            if receiver in receivers:
                if receiver not in friends[username]:
                    await send_msg(writer, pubkeys[receiver])
                    friends[username].add(receiver)
                msg = await read_msg(reader, False)
                print(f'Sending to {receiver}: {msg[:20]}...')
                await send_msg(receivers[receiver], msg, False) 
            else:
                await send_msg(writer, f'User {receiver} is offline')
    except asyncio.CancelledError:
        print(f'Remote {peername} closing connection.')
        writer.close()
        await writer.wait_closed()
    except asyncio.IncompleteReadError:
        print(f'Remote {peername} disconnected')
    finally:
        print(f'Remote {peername} closed')
        del receivers[username]

async def main(*args, **kwargs):
    server = await asyncio.start_server(*args, **kwargs)
    async with server:
        await server.serve_forever()

try:
    asyncio.run(main(handle_connection, host='127.0.0.1', port=8888))
except KeyboardInterrupt:
    print()
    print('Bye!')
