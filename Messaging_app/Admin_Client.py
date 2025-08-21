import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
import socket
import threading
from cryptography.fernet import Fernet
from dotenv import load_dotenv
load_dotenv()
import os

# Client configuration
HOST = os.getenv("client_HOST")
PORT = int(os.getenv("PORT"))  # Port to connect to the server

class ChatClient:
    def __init__(self, master):
        self.master = master
        master.title("Dark Path by Daniyal")
        master.geometry("500x800")
        master.minsize(400, 600)
        master.configure(bg="#2C3E50")

        self.username = ""  # Initialize username as empty
        self.secret_key = b'pJSJnJuppVabvm4yKpOJ610CScLinR8dtnOV09ZMWx8='  # Replace with your actual key
        self.cipher = Fernet(self.secret_key)
        self.login_screen()

    def login_screen(self):
        # Clear previous widgets
        for widget in self.master.winfo_children():
            widget.destroy()

        # Login Screen UI
        self.login_frame = tk.Frame(self.master, bg="#2C3E50", pady=10)
        self.login_frame.pack(fill=tk.BOTH, expand=True)

        # App Title
        self.app_title = tk.Label(self.login_frame, text="Dark Path", font=("Helvetica", 30, "bold"), fg="#ECF0F1", bg="#2C3E50")
        self.app_title.pack(pady=10)

        self.login_label = tk.Label(self.login_frame, text="Enter Your Username", font=("Helvetica", 20, "bold"), bg="#2C3E50", fg="#ECF0F1")
        self.login_label.pack(pady=10)

        # Username Entry
        self.username_entry = tk.Entry(self.login_frame, font=("Helvetica", 14), bg="#ECF0F1", fg="#2C3E50", bd=0, relief="flat", justify="center")
        self.username_entry.pack(pady=10, ipadx=10, ipady=10)
        self.username_entry.bind("<FocusIn>", self.on_focus_in)
        self.username_entry.bind("<FocusOut>", self.on_focus_out)

        # Join Button
        self.login_button = tk.Button(self.login_frame, text="Join Chat", font=("Helvetica", 14, "bold"), bg="#1ABC9C", fg="white", command=self.on_login, relief="flat", width=20)
        self.login_button.pack(pady=20)

        # "By Daniyal" Footer
        self.footer_label = tk.Label(self.login_frame, text="By Daniyal", font=("Helvetica", 10), fg="#ECF0F1", bg="#2C3E50")
        self.footer_label.pack(side=tk.BOTTOM, pady=20)

    def on_focus_in(self, event):
        event.widget.config(bg="#dff9f1", fg="#2C3E50")

    def on_focus_out(self, event):
        event.widget.config(bg="#ECF0F1", fg="#2C3E50")

    def on_login(self):
        username = self.username_entry.get().strip()

        if not username:
            messagebox.showerror("Invalid Username", "Please enter a valid username.")
            return

        # Set the username and move to chat screen
        self.username = username
        self.setup_chat_screen()

        # Send the username to the server
        self.client_socket.send(self.cipher.encrypt(self.username.encode('utf-8')))

    def setup_chat_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        master = self.master
        master.title("Dark Path by Daniyal")
        master.geometry("500x800")
        master.minsize(400, 600)
        master.configure(bg="#2C3E50")

        # Header
        self.header = tk.Label(master, text="Welcome to Dark Path", font=("Helvetica", 16, "bold"), bg="#1ABC9C", fg="white", pady=20)
        self.header.pack(fill=tk.X)

        # Profile Section
        self.profile_frame = tk.Frame(master, bg="#34495E", pady=10)
        self.profile_frame.pack(fill=tk.X)
        
        self.profile_icon = tk.Label(self.profile_frame, text="👤", font=("Helvetica", 40), fg="white", bg="#34495E")
        self.profile_icon.pack(side=tk.LEFT, padx=10)

        self.username_label = tk.Label(self.profile_frame, text="Username: ", font=("Helvetica", 12), fg="white", bg="#34495E")
        self.username_label.pack(side=tk.LEFT)

        self.username_display = tk.Label(self.profile_frame, text=self.username, font=("Helvetica", 12, "bold"), fg="white", bg="#34495E")
        self.username_display.pack(side=tk.LEFT)

        # User Count Display
        self.user_count_label = tk.Label(self.profile_frame, text="Users: 0", font=("Helvetica", 12, "bold"), fg="white", bg="#34495E")
        self.user_count_label.pack(side=tk.LEFT, padx=20)

        # Chat display area
        self.chat_area = scrolledtext.ScrolledText(master, state='disabled', wrap='word', bg="#2C3E50", fg="#ECF0F1", font=("Helvetica", 12))
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Recipient entry
        self.recipient_frame = tk.Frame(master, bg="#34495E")
        self.recipient_frame.pack(padx=10, pady=(5, 0), fill=tk.X)
        self.recipient_label = tk.Label(self.recipient_frame, text="Sender (leave blank for public message):", bg="#34495E", fg="white", font=("Helvetica", 10))
        self.recipient_label.pack(side=tk.LEFT)
        self.recipient_entry = tk.Entry(self.recipient_frame, bg="#ECF0F1", fg="#2C3E50", font=("Helvetica", 12))
        self.recipient_entry.pack(side=tk.RIGHT, fill=tk.X, expand=True)

        # Message entry
        self.message_frame = tk.Frame(master, bg="#34495E")
        self.message_frame.pack(padx=10, pady=(10, 0), fill=tk.X)
        self.message_label = tk.Label(self.message_frame, text="Your Message:", bg="#34495E", fg="white", font=("Helvetica", 10))
        self.message_label.pack(side=tk.LEFT)
        self.message_entry = tk.Entry(self.message_frame, bg="#ECF0F1", fg="#2C3E50", font=("Helvetica", 12))
        self.message_entry.pack(side=tk.RIGHT, fill=tk.X, expand=True)
        self.message_entry.bind("<Return>", self.send_message)

        # Send button
        self.send_button = tk.Button(master, text="Send", bg="#1ABC9C", fg="white", font=("Helvetica", 12, "bold"), command=self.send_message)
        self.send_button.pack(padx=10, pady=10, fill=tk.X)

        # Connect to server
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect((HOST, PORT))
        except Exception as e:
            messagebox.showerror("Connection Error", f"Could not connect to server: {e}")
            master.destroy()
            return

        threading.Thread(target=self.receive_messages, daemon=True).start()

    def send_message(self, event=None):
        if not self.username:
            messagebox.showerror("Username Required", "You must enter a valid username to send a message.")
            return

        recipient = self.recipient_entry.get().strip()
        message = self.message_entry.get().strip()

        if message:
            if recipient:
                formatted_message = f"{recipient}:{message}"
            else:
                formatted_message = message
            try:
                encrypted_message = self.cipher.encrypt(formatted_message.encode('utf-8'))
                self.client_socket.send(encrypted_message)
                self.chat_area.config(state='normal')
                self.chat_area.insert(tk.END, f"You: {message}\n")
                self.chat_area.config(state='disabled')
                self.chat_area.see(tk.END)  # Scroll to the bottom
                self.message_entry.delete(0, tk.END)
            except Exception as e:
                messagebox.showerror("Send Error", f"Failed to send message: {e}")

    def receive_messages(self):
        while True:
            try:
                encrypted_message = self.client_socket.recv(1024)
                if encrypted_message:
                    print(f"Received encrypted message: {encrypted_message}")
                    try:
                        message = self.cipher.decrypt(encrypted_message).decode('utf-8')
                        print(f"Decrypted message: {message}")
                        if "has joined the chat" not in message and "has left the chat" not in message:
                            if message.startswith("USER_COUNT:"):
                                user_count = message.split(":")[1]
                                self.user_count_label.config(text=f"Users: {user_count}")
                            else:
                                self.chat_area.config(state='normal')
                                self.chat_area.insert(tk.END, message + "\n")
                                self.chat_area.config(state='disabled')
                                self.chat_area.see(tk.END)
                    except Exception as e:
                        print(f"Error decrypting message: {e}")
                        print(f"Encrypted message: {encrypted_message}")
            except Exception as e:
                print(f"Error receiving message: {e}")
                break

if __name__ == "__main__":
    root = tk.Tk()
    client = ChatClient(root)
    root.mainloop()