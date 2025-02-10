import socket
import threading

HOST = '127.0.0.1'  # Adresse locale
PORTS = [22, 5050]  # Ports à écouter

def start_server(port):
    """Crée un serveur qui écoute sur un port donné"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, port))
    server.listen(5)
    print(f"📡 Serveur en écoute sur {HOST}:{port}...")

    while True:
        client, addr = server.accept()
        print(f"✅ Connexion reçue de {addr} sur le port {port}")
        client.send(f"Hello! Port {port} actif.\n".encode())
        client.close()

# Lancer un thread pour chaque port
for port in PORTS:
    threading.Thread(target=start_server, args=(port,), daemon=True).start()

# Garder le programme actif
try:
    while True:
        pass
except KeyboardInterrupt:
    print("\n🛑 Serveur arrêté.")
