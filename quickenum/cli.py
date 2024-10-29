from scanners.nmap_scan import scan_host, check_for_http
import argparse


from rich import box
from rich.console import Console
from rich.table import Table

#ciekawe biblioteki do wykorzystania pozniej:
#rich(kolorowanie terminala), typer/click (ogolne ulepszeni CLI)
#yaspin/tqdm (progress indicators), pyfiglet(ASCII art), tabulate (nice tables), inquirer (interaktywny terminal)

console = Console()

def show_service_table(services):

    data_table = Table(title="Service Information", box=box.DOUBLE_EDGE)
    data_table.add_column("Port")
    data_table.add_column("State", style="green")
    data_table.add_column("Name")
    data_table.add_column("Product")

    for service in services:
        data_table.add_row(str(service["Port"]),service["State"], service["Name"], service["Product"])

    console.print(data_table)

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







