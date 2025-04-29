import requests
from colorama import Fore, Style

def analyze_http(target):
    url = f"http://{target}"
    try:
        response = requests.get(url, timeout=3)
        
        print(Fore.CYAN + f"\n[+] HTTP Response from {url}:" + Style.RESET_ALL)
        print(f"Status Code: {response.status_code}")
        
        server = response.headers.get('Server', 'Unknown')
        print(f"Server: {server}")

        print("\n[+] Security Headers:")
        security_headers = [
            "Content-Security-Policy",
            "Strict-Transport-Security",
            "X-Frame-Options",
            "X-XSS-Protection",
            "X-Content-Type-Options",
            "Referrer-Policy"
        ]
        for header in security_headers:
            value = response.headers.get(header)
            if value:
                print(Fore.GREEN + f"  [+] {header}: {value}" + Style.RESET_ALL)
            else:
                print(Fore.RED + f"  [-] {header}: Missing" + Style.RESET_ALL)

    except requests.RequestException as e:
        print(Fore.RED + f"[!] Failed to connect to {url}: {e}" + Style.RESET_ALL)