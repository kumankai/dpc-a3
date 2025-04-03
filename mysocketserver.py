import socket
import threading
import Pyro4


def handle_client(client_socket, pyro_server):
    try:
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break

            # Parse operation and numbers
            parts = data.strip().split()
            if len(parts) < 2:
                client_socket.send("Invalid request".encode())
                continue

            operation = parts[0].lower()
            numbers = list(map(float, parts[1:]))

            # Perform requested operation via Pyro4
            try:
                if operation == "add":
                    result = pyro_server.add(*numbers)
                elif operation == "sub":
                    result = pyro_server.subtract(*numbers)
                elif operation == "mul":
                    result = pyro_server.multiply(*numbers)
                elif operation == "div":
                    result = pyro_server.divide(*numbers)
                elif operation == "mod":
                    result = pyro_server.modulus(*numbers)
                elif operation == "sqrt":
                    result = pyro_server.sqrt(numbers[0])
                else:
                    result = "Unknown operation"
            except Exception as e:
                result = f"Error: {str(e)}"

            client_socket.send(str(result).encode())
    except Exception as e:
        print(f"Client error: {e}")
    finally:
        client_socket.close()


def start_socket_server(host=socket.gethostname(), port=4000):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Socket Server listening on {host}:{port}")

    # Connect to Pyro4 server
    pyro_server = Pyro4.Proxy("PYRONAME:math.operations")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(
            target=handle_client, args=(client_socket, pyro_server))
        client_handler.start()


if __name__ == "__main__":
    start_socket_server()
