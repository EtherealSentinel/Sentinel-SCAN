import requests
from colorama import Fore, Style

def dir_brute_force(target, wordlist_path="wordlist\common.txt"):
    url_base = f"http://{target}/"

    try:
        with open(wordlist_path, "r") as wordlist:
            print(Fore.YELLOW + f"\n[*] Starting directory brute force on {url_base}\n" + Style.RESET_ALL)
            for line in wordlist:
                word = line.strip()
                full_url = url_base + word
                try:
                    response = requests.get(full_url, timeout=3)
                    if response.status_code == 200:
                        print(Fore.GREEN + f"[+] Found: {full_url}" + Style.RESET_ALL)
                    elif response.status_code in [401, 403]:
                        print(Fore.CYAN + f"[?] Restricted: {full_url} ({response.status_code})" + Style.RESET_ALL)
                except requests.RequestException:
                    continue

    except FileNotFoundError:
        print(Fore.RED + f"[!] Wordlist not found: {wordlist_path}" + Style.RESET_ALL)