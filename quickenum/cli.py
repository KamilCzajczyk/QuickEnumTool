import nmap
import subprocess

def scanhost(host):
    nm = nmap.PortScanner()
    #default scan -> nmap -oX -sV <IP>
    nm.scan(host, arguments="-sV")
    print(f"Command used for scan: {nm.command_line()}")



def main():
    print("Welcome to QuickScan")
    ip = input("Input IP Address: ")
    scanhost(ip)

if __name__ == '__main__':
    main()







