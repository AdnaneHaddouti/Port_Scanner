import socket

def scan_port(ip, port):
    """Vérifie si un port est ouvert sur une IP donnée"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)  # Timeout pour éviter de bloquer le script
    result = s.connect_ex((ip, port))  # Renvoie 0 si le port est ouvert
    s.close()
    return result == 0

def main():
    target = input("Entrez l'adresse IP cible : ")
    ports = [21, 22, 25, 53, 80, 443, 3306, 8080, 5050]  # Liste de ports à scanner
    
    print(f"\nScan en cours sur {target}...\n")
    for port in ports:
        if scan_port(target, port):
            print(f"[+] Port {port} est **OUVERT** ✅")
        else:
            print(f"[-] Port {port} est fermé ❌")

if __name__ == "__main__":
    main()