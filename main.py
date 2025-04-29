import argparse
from scanner import ports, http_info  # http_info added
from scanner import ports, http_info, dir_brute #bruteforce module added


def banner():
    print("=" * 50)
    print("🛡️  Sentinel-Scan - Basic Recon Tool")
    print("Author: EtherealSentinel")
    print("=" * 50)

def main():
    banner()
    
    parser = argparse.ArgumentParser(description="Basic Red Team Recon Tool")
    parser.add_argument("target", help="Target IP or domain to scan")
    args = parser.parse_args()

    print(f"\n[+] Starting scan on target: {args.target}\n")
    
    ports.scan_ports(args.target)
    http_info.analyze_http(args.target)
    dir_brute.dir_brute_force(args.target)

if __name__ == "__main__":
    main()