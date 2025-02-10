#cree un script qui scan les ports d'une switch et affiche les ports ouverts
import socket
import sys

def scan_ports(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((host, port))
        s.close()
        return True
    except:
        return False
    

def main():
    host = sys.argv[1]
    for port in range(1, 1025):
        if scan_ports(host, port):
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")


            
