# 🔒 Dark Path (Encrypted Messaging System)

**Dark Path** is a multi-threaded, encrypted client-server messaging application built entirely in Python. It demonstrates foundational knowledge of low-level networking, concurrent threading, and applied cryptography.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Cryptography-Fernet-black?style=for-the-badge" alt="Cryptography">
  <img src="https://img.shields.io/badge/Sockets-TCP%2FIP-green?style=for-the-badge" alt="Sockets">
</p>

---

## 🏗️ Technical Architecture & Key Features

This project was built to explore how data is securely transmitted across networks before relying on higher-level web frameworks (like HTTPS/WebSockets).

### 1. Concurrent Socket Server
- **Networking:** Built using Python's native `socket` library leveraging the TCP protocol for reliable packet delivery.
- **Concurrency:** Implements multi-threading (`threading` library) to handle numerous simultaneous client connections without blocking the main server thread.

### 2. End-to-End Encryption (E2EE)
- **Security:** Integrated the `cryptography.fernet` symmetric encryption module. 
- **Data Protection:** All messages sent over the TCP socket are encrypted before transmission and decrypted strictly client-side. The server acts purely as a router and cannot read the raw packet data in transit.

### 3. Graphical User Interface (GUI)
- **Frontend Engine:** Built with `tkinter`, moving beyond basic CLI to a full windowed application.
- **UX Design:** Features a login system, active user counting, private messaging functionality routing (`User:Message`), and a custom "Cyber Dark" aesthetic (`bg="#2C3E50"`).

---

## 💡 Skills Demonstrated
- **Low-Level Networking:** Deep understanding of TCP handshakes, binding, listening, and accepting socket connections.
- **Concurrency & Threads:** Managing shared memory states safely across spawned threads.
- **Security Engineering:** Applied concepts of symmetric key cryptography ensuring data privacy over local networks.

---

## 🛠️ Local Setup

1. **Clone the repository:**
```bash
git clone https://github.com/YOUR_USERNAME/Messaging_app.git
cd Messaging_app
```

2. **Install requirements:**
```bash
pip install cryptography python-dotenv
```

3. **Environment Setup:**
Create a `.env` file referencing your `HOST`, `client_HOST`, and `PORT`.

4. **Run the Server:**
Launch the listener in your terminal:
```bash
python Server.py
```

5. **Run the Client:**
Launch one (or multiple) client instances to connect:
```bash
python Client_App.py
```

---

## 👨‍💻 About The Developer

Built by **Daniyal Rashid**. I specialize in creating secure backend architectures and full-stack solutions. 

🔗 **[View My Portfolio & Resume](https://daniyal-rashid.vercel.app/)**
