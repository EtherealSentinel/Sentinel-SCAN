import socket
from colorama import Fore, Style

common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL"
}

def scan_ports(target):
    print(Fore.YELLOW + "[*] Scanning common ports...\n" + Style.RESET_ALL)
    for port, service in common_ports.items():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(Fore.GREEN + f"[+] Open: {port}/tcp ({service})" + Style.RESET_ALL)
            else:
                print(Fore.RED + f"[-] Closed: {port}/tcp ({service})" + Style.RESET_ALL)
            sock.close()
        except Exception as e:
            print(Fore.MAGENTA + f"[!] Error on port {port}: {e}" + Style.RESET_ALL)
