import subprocess


def convert_to_url(ip):
    return f"http://{ip}"

def gobuster_scan(host, wordlist):
    command = ["gobuster", "dir","-w", wordlist,"-u",host]
    command_str = " ".join(command)
    #process = subprocess.run(command,capture_output=True, text=True, check=True)
    print(host)
    print(command_str)
