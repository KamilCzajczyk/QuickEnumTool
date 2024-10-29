import nmap
import argparse


from rich import box
from rich.console import Console
from rich.table import Table

#ciekawe biblioteki do wykorzystania pozniej:
#rich(kolorowanie terminala), typer/click (ogolne ulepszeni CLI)
#yaspin/tqdm (progress indicators), pyfiglet(ASCII art), tabulate (nice tables), inquirer (interaktywny terminal)

common_http_ports = {
    66, 80, 81, 443, 445, 457, 1080, 1100, 1241, 1352, 1433, 1434,
    1521, 1944, 2301, 3000, 3128, 3306, 4000, 4001, 4002, 4100, 5000,
    5432, 5800, 5801, 5802, 6346, 6347, 7001, 7002, 8000, 8080, 8443,
    8888, 30821
}
console = Console()
def scan_host(host):
    nm = nmap.PortScanner()
    #default scan -> nmap -oX -sV <IP>
    print(f"[+] Performing nmap scan on {host} with Nmap{nm.nmap_version()}")
    nm.scan(host, arguments="-sV")
    #print(f"[+] Command used for scan: {nm.command_line()}")
    all_services = []

    if nm[host].state() == "down":
       print("[-] Host seems down, check for errors and try again.")
    else:

        print("[+] Host is up")
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


def show_service_table(services):

    data_table = Table(title="Service Information", box=box.DOUBLE_EDGE)
    data_table.add_column("Port")
    data_table.add_column("State", style="green")
    data_table.add_column("Name")
    data_table.add_column("Product")

    for service in services:
        data_table.add_row(str(service["Port"]),service["State"], service["Name"], service["Product"])

    console.print(data_table)

def check_for_http(services):
    found = False
    for service in services:
        if service["Port"] in common_http_ports:
            found = True
            return found







def main():
    #print("Welcome to QuickScan")
    parser = argparse.ArgumentParser(description="Quick Enum Tool")
    parser.add_argument('host', help='IP to enumerate')


    args = parser.parse_args()
    #ip = input("Input IP Address: ")

    scan_result = scan_host(args.host)
    
    show_service_table(scan_result)
    if check_for_http(scan_result):
        console.print("[!] Http/Https found!")


if __name__ == '__main__':
    main()







