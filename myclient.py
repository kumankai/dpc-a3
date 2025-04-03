import socket

def main():
    host = socket.gethostname()
    port = 4000

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            print("Connected to the server.")
            
            while True:
                print("Enter math operation <OPERATION> x y")
                print("['add', 'sub', 'mul', 'div', 'mod', 'sqrt', 'exit']\n")
                operation = input("").strip()
                
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
