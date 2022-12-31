from asyncio import StreamReader, StreamWriter

async def read_msg(reader, decode=True):
    size_bytes = await reader.readexactly(4)
    size = int.from_bytes(size_bytes, byteorder='big')
    data = await reader.readexactly(size)
    if decode:
        data = data.decode()
    return data

async def send_msg(writer, data, encode=True):
    if encode:
        data = data.encode()
    size_bytes = len(data).to_bytes(4, byteorder='big')
    writer.writelines([size_bytes, data])
    await writer.drain()
