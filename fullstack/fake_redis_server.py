"""Локальный фейковый Redis-сервер (fakeredis) для разработки без установленного Redis."""
from fakeredis import TcpFakeServer

if __name__ == "__main__":
    server = TcpFakeServer(("127.0.0.1", 6379), server_type="redis", server_version=(7, 0))
    print("Fake Redis listening on 127.0.0.1:6379")
    server.serve_forever()
