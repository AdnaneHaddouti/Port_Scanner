import socket
import threading

HOST = '127.0.0.1'  # Adresse locale
PORTS = [22, 5050]  # Ports à écouter

def start_server(port):
    """Crée un serveur qui écoute sur un port donné"""
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Permet de réutiliser le port immédiatement
        server.bind((HOST, port))
        server.listen(5)
        print(f"📡 Serveur en écoute sur {HOST}:{port}...")

        while True:
            client, addr = server.accept()
            print(f"✅ Connexion reçue de {addr} sur le port {port}")
            client.send(f"Hello! Port {port} actif.\n".encode())
            client.close()
    except Exception as e:
        print(f"⚠️ Erreur sur le port {port}: {e}")

# Lancer un thread pour chaque port
threads = []
for port in PORTS:
    thread = threading.Thread(target=start_server, args=(port,), daemon=True)
    thread.start()
    threads.append(thread)

# Garder le programme actifqsQS
try:
    while True:
        pass
except KeyboardInterrupt:
    print("\n🛑 Serveur arrêté.")