import socket

HOST = '100.87.237.32'  
PORT = 5000

# TCP socket
# AF_INET: IPv4, SOCK_STREAM: TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    
    # Bind: configuring the socket with the IP
    server_socket.bind((HOST, PORT))
    
    # Listen: The server waits for connections
    server_socket.listen()
    print(f"The server is running on {HOST}, port {PORT}...")
    
    # Outer loop to keep the server running for new connections
    while True:
        # Accept: Blocking call until a client connects
        client_socket, client_address = server_socket.accept()
        
        with client_socket:
            print(f"\n--- Connection established successfully from: {client_address} ---")
            
            # Inner loop to continuously receive messages from the connected client
            while True:
                # Receive data from the client (buffer size is 1024 bytes)
                data = client_socket.recv(1024)
                
                # If data is empty, the client has disconnected
                if not data:
                    print(f"--- Client {client_address} disconnected ---")
                    break
                    
                # Decoding the message using UTF-8
                text_message = data.decode('utf-8')
                print(f"Message received from client {client_address}: {text_message}")