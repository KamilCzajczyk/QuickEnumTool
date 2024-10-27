import nmap

from rich.console import Console
from rich.table import Table

#ciekawe biblioteki do wykorzystania pozniej:
#rich(kolorowanie terminala), typer/click (ogolne ulepszeni CLI)
#yaspin/tqdm (progress indicators), pyfiglet(ASCII art), tabulate (nice tables), inquirer (interaktywny terminal)


def scan_host(host):
    nm = nmap.PortScanner()
    #default scan -> nmap -oX -sV <IP>
    print(f"[+] Performing nmap scan on {host} with Nmap{nm.nmap_version()}")
    nm.scan(host, arguments="-sV")
    print(f"[+] Command used for scan: {nm.command_line()}")

    if nm[host].state() == "down":
       print("[-] Host seems down, check for errors and try again.")
    else:
        print("[+] Host is up")
        for protocol in nm[host].all_protocols():
            print(f"[+] {protocol}")
            l_port = nm[host][protocol]

            for port in l_port:
                print(f"port : {port}\tstate : {nm[host][protocol][port]['state']}")





def http_found():
    return 1

def main():
    print("Welcome to QuickScan")
    ip = input("Input IP Address: ")
    scan_host(ip)



if __name__ == '__main__':
    main()







