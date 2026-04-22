import socket

HOST = '100.87.237.32'  
PORT = 5000

# UDP socket
# AF_INET: IPv4, SOCK_DGRAM: UDP socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    
    # Bind: configuring the socket with the IP
    server_socket.bind((HOST, PORT))
    
    print(f"The UDP server is running on {HOST}, port {PORT}...")
    
    # Loop to continuously receive messages from any client
    while True:
        # recvfrom returns the data and the address of the sender
        data, client_address = server_socket.recvfrom(1024)
        
        if data:
            # Decoding the message using UTF-8
            text_message = data.decode('utf-8')
            print(f"Message received from client {client_address}: {text_message}")