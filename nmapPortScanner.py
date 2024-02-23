import nmap

nmap = nmap.PortScanner()

host_domain = input("[-] Enter Target Domain: ") # take in the domain/target

ports = input("[+] Enter Port(s) you want to scan: ") # ports to scan on the domain

if ports == "":
    ports = "20-1024"

print(f"Scanning Port(s): {ports}")
nmap.scan(host_domain, ports)

for host in nmap.all_hosts():
    for protocol in nmap[host].all_protocols():
        print(f"[+] Protocol used by host: {protocol}")
        ports_for_proto = nmap[host][protocol].keys()
        for port in ports_for_proto:
            print(f"[+] Port: {port}\t", end='')
            print(f"[+] State: {nmap[host][protocol][port]['state']}")

print("\n")
print("[+] Scan Complete")

