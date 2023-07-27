import asyncio

async def send_data(reader):
    while True:
        data = await reader.read(100)
        if not data:
            break

        message = data.decode()
        if not message.startswith("Server received"):
            print(f"Received from server: {message}")

async def send_messages(writer, username):
    try:
        while True:
            message = await asyncio.get_event_loop().run_in_executor(None, input, "Enter message to send (or 'exit' to quit): ")
            if message.lower() == 'exit':
                break

            writer.write(f"{username}: {message}\n".encode())
            await writer.drain()
    finally:
        writer.close()

async def main():
    server_address = 'localhost'
    server_port = 8888

    username = input("Enter your username: ")

    reader, writer = await asyncio.open_connection(server_address, server_port)

    try:
        await asyncio.gather(send_data(reader), send_messages(writer, username))
    finally:
        writer.close()
        await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
