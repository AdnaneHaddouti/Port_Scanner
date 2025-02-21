import socket
from datetime import datetime
import concurrent.futures

IMPORTANT_PORTS = {
    20: "FTP-Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP-Server",
    68: "DHCP-Client",
    69: "TFTP",
    80: "HTTP",
    110: "POP3",
    119: "NNTP",
    123: "NTP",
    135: "MS-RPC",
    139: "NetBIOS",
    143: "IMAP",
    161: "SNMP",
    194: "IRC",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    465: "SMTPS",
    514: "Syslog",
    587: "SMTP-Submission",
    636: "LDAPS",
    993: "IMAPS",
    995: "POP3S",
    1080: "SOCKS",
    1433: "MSSQL",
    1521: "OracleDB",
    2049: "NFS",
    3306: "MySQL",
    3389: "RDP",
    5060: "SIP",
    5222: "XMPP",
    5432: "PostgreSQL",
    5900: "VNC",
    5938: "TeamViewer",
    6379: "Redis",
    6667: "IRC",
    8000: "HTTP-Alt",
    8080: "HTTP-Proxy",
    8443: "HTTPS-Alt",
    8888: "Sun-Alt",
    9000: "PhpMyAdmin",
    9090: "WebSM",
    9100: "Print-Server",
    9200: "Elasticsearch",
    27017: "MongoDB",
    27018: "MongoDB-Shard",
    27019: "MongoDB-Router",
    28015: "RethinkDB",
    25565: "Minecraft"
}

def get_target():
    hostname = input("Enter target hostname/IP: ").strip()
    try:
        target = socket.gethostbyname(hostname)
        print(f"\nTarget: {target}")
        print(f"Scanning {len(IMPORTANT_PORTS)} key ports...\n")
        return target
    except socket.gaierror:
        print("Error: Hostname resolution failed")
        exit(1)

def scan_port(target, port, timeout=1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            if s.connect_ex((target, port)) == 0:
                try:
                    service = socket.getservbyport(port) or IMPORTANT_PORTS.get(port, "Unknown")
                except OSError:
                    service = IMPORTANT_PORTS.get(port, "Unknown")
                return (port, service)
    except (socket.timeout, ConnectionRefusedError):
        pass
    except Exception as e:
        pass
    return None

def port_scanner():
    start_time = datetime.now()
    try:
        target = get_target()
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
            futures = {executor.submit(scan_port, target, port): port for port in IMPORTANT_PORTS}
            open_ports = []
            
            for future in concurrent.futures.as_completed(futures):
                port = futures[future]
                result = future.result()
                if result:
                    open_ports.append(result)
                    print(f"• Port {result[0]:<5} [{result[1]:<20}] OPEN✅")

        duration = datetime.now() - start_time
        print(f"\nScan completed in {duration.total_seconds():.2f} seconds")
        print(f"Found {len(open_ports)} open ports")
        
    except KeyboardInterrupt:
        print("\nScan interrupted by user!")
    except Exception as e:
        print(f"\nError: {e}")

if __name__ == '__main__':
    port_scanner()