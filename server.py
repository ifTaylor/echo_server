import asyncio

clients = {}

class EchoServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print(f"Connection from {peername}")
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        peername = self.transport.get_extra_info('peername')
        print(f"{message}")

        self.transport.write(f"Server received: {message}".encode())

        for client_transport in clients.values():
            if client_transport != self.transport:
                client_transport.write(data)

    def connection_lost(self, exc):
        peername = self.transport.get_extra_info('peername')
        print(f"Connection closed from {peername}")
        del clients[peername]

    async def handle_client(self, transport):
        while True:
            await asyncio.sleep(1)

async def main():
    server_port = 8888
    loop = asyncio.get_event_loop()

    server = await loop.create_server(
        EchoServerProtocol,
        'localhost',
        server_port
    )
    print(f"Server started on localhost:{server_port}")

    try:
        await asyncio.gather(server.serve_forever())
    except KeyboardInterrupt:
        pass
    finally:
        for task in clients.values():
            task.cancel()
        server.close()
        await server.wait_closed()
        print("Server closed")

if __name__ == "__main__":
    asyncio.run(main())
