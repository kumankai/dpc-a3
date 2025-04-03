import socket

def main():
    host = "localhost"  # Change if running in Docker or different machine
    port = 5000         # Must match `mysocketserver.py`

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            print("Connected to the server.")
            
            while True:
                operation = input("Enter math operation (e.g., 'add 5 3') or 'exit' to quit: ").strip()
                
                if operation.lower() == "exit":
                    break
                
                client_socket.sendall(operation.encode())
                result = client_socket.recv(1024).decode()
                
                print("Result:", result)

    except ConnectionRefusedError:
        print("Error: Could not connect to the server. Ensure the socket server is running.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
