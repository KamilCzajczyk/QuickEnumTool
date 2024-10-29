from scanners.nmap_scan import scan_host, check_for_http
from scanners.gobuster_scan import gobuster_scan, convert_to_url

import argparse

from rich import box
from rich.console import Console
from rich.table import Table

#ciekawe biblioteki do wykorzystania pozniej:
#rich(kolorowanie terminala), typer/click (ogolne ulepszeni CLI)
#yaspin/tqdm (progress indicators), pyfiglet(ASCII art), tabulate (nice tables), inquirer (interaktywny terminal)

console = Console()

def show_service_table_from_nmap(services):

    data_table = Table(title="Nmap Scan Service Information", box=box.DOUBLE_EDGE)
    data_table.add_column("Port")
    data_table.add_column("State", style="green")
    data_table.add_column("Name")
    data_table.add_column("Product")

    for service in services:
        data_table.add_row(str(service["Port"]),service["State"], service["Name"], service["Product"])

    console.print(data_table)

def main():

    parser = argparse.ArgumentParser(description="Quick Enum Tool")
    parser.add_argument('host', help='IP to enumerate')
    parser.add_argument('wordlist', help='Wordlist for http enumeration',type=str,default='/usr/share/wordlists/dirb/common.txt')

    args = parser.parse_args()

    scan_result = scan_host(args.host)
    
    show_service_table_from_nmap(scan_result)

    if check_for_http(scan_result):
        #console.print("[!] Http/Https found!")
        gobuster_scan(convert_to_url(args.host),args.wordlist)



if __name__ == '__main__':
    main()







