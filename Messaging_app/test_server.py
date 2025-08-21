import socket
import threading
from cryptography.fernet import Fernet
from dotenv import load_dotenv
load_dotenv()
import os

# Server configuration
HOST = os.getenv("HOST")  # Listen on all interfaces
PORT = int(os.getenv("PORT"))       # Port to listen on
secret_key = b'pJSJnJuppVabvm4yKpOJ610CScLinR8dtnOV09ZMWx8='  # Replace with your actual key

# Use this Code to generate new keys if you want:

# from cryptography.fernet import Fernet
# # Generate a new Fernet key
# new_key = Fernet.generate_key()
# # Print the generated key
# print(new_key.decode())

cipher = Fernet(secret_key)

# Dictionary to keep track of connected clients
clients = {}
usernames = {}

# Broadcasts a message to all connected clients
def broadcast(message, sender=None):
    encrypted_message = cipher.encrypt(message.encode('utf-8'))
    for client_socket in clients:
        if clients[client_socket] != sender:
            client_socket.send(encrypted_message)

# Sends a user count message to all clients
def send_user_count():
    user_count_message = f"USER_COUNT:{len(clients)}"
    encrypted_message = cipher.encrypt(user_count_message.encode('utf-8'))
    for client_socket in clients:
        client_socket.send(encrypted_message)

# Handles a single client connection
def handle_client(client_socket):
    try:
        # Get the username from the client
        encrypted_username = client_socket.recv(1024)
        username = cipher.decrypt(encrypted_username).decode('utf-8')
        if username in usernames:
            client_socket.send(cipher.encrypt("Username already taken. Disconnecting.".encode('utf-8')))
            client_socket.close()
            return

        clients[client_socket] = username
        usernames[username] = client_socket
        print(f"{username} has connected.")
        
        # Broadcast join message without the user count
        broadcast(f"{username} has joined the chat.", sender=None)
        
        # Send the current user count separately
        send_user_count()

        while True:
            encrypted_message = client_socket.recv(1024)
            if not encrypted_message:
                break

            message = cipher.decrypt(encrypted_message).decode('utf-8')

            # Log all messages to the server
            log_message(username, message)

            # Check for private messages
            if ':' in message:
                recipient, msg = message.split(':', 1)
                send_private_message(username, recipient.strip(), msg.strip())
            else:
                broadcast(f"{username}: {message}", sender=username)

    except Exception as e:
        print(f"Error handling client {username}: {e}")
    finally:
        # Clean up when the client disconnects
        disconnect_client(client_socket)

# Logs messages to the server console
def log_message(sender, message):
    print(f"Log - {sender} to {message}")

# Sends a private message to a specific user
def send_private_message(sender, recipient, message):
    if recipient in usernames:
        recipient_socket = usernames[recipient]
        encrypted_message = cipher.encrypt(f"{sender}: {message}".encode('utf-8'))
        recipient_socket.send(encrypted_message)
    else:
        sender_socket = usernames[sender]
        encrypted_message = cipher.encrypt(f"User {recipient} not found.".encode('utf-8'))
        sender_socket.send(encrypted_message)

# Handles disconnecting clients
def disconnect_client(client_socket):
    username = clients.get(client_socket, "Unknown")
    print(f"{username} has disconnected.")
    client_socket.close()
    if client_socket in clients:
        del clients[client_socket]
    if username in usernames:
        del usernames[username]
    broadcast(f"{username} has left the chat.", sender=None)

# Starts the server
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print("Server started. Waiting for connections...")
    try:
        while True:
            client_socket, addr = server_socket.accept()
            threading.Thread(target=handle_client, args=(client_socket,), daemon=True).start()
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()