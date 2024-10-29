import nmap
from rich.console import Console
console = Console()

common_http_ports = {
    66, 80, 81, 443, 445, 457, 1080, 1100, 1241, 1352, 1433, 1434,
    1521, 1944, 2301, 3000, 3128, 3306, 4000, 4001, 4002, 4100, 5000,
    5432, 5800, 5801, 5802, 6346, 6347, 7001, 7002, 8000, 8080, 8443,
    8888, 30821
}

def scan_host(host):
    nm = nmap.PortScanner()
    #default scan -> nmap -oX -sV <IP>
    console.print(f"[+] Performing nmap scan on {host} with Nmap{nm.nmap_version()}",style="blue")
    nm.scan(host, arguments="-sV")
    #print(f"[+] Command used for scan: {nm.command_line()}")
    all_services = []

    if nm[host].state() == "down":
       console.print("[-] Host seems down, check for errors and try again.", style="bold red")
    else:

        console.print("[+] Host is up",style="green")
        for protocol in nm[host].all_protocols():
            #print(f"[+] {protocol}")
            l_port = nm[host][protocol]
            #print(f'porty: {nm[host][protocol].keys()}')
            for port in l_port:
                port_info = {
                    "Port": port,
                    "State": nm[host][protocol][port]['state'],
                    "Name": nm[host][protocol][port]['name'],
                    "Product": nm[host][protocol][port]['product'],
                }
                all_services.append(port_info)

    return all_services


def check_for_http(services):
    found = False
    for service in services:
        if service["Port"] in common_http_ports:
            found = True
            return found