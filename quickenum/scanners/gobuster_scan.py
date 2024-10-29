import subprocess
import re


def convert_to_url(ip):
    return f"http://{ip}"

def gobuster_scan(host, wordlist):
    command = ["gobuster", "dir","-w", wordlist,"-u",host]
    process = subprocess.run(command, stdout=subprocess.PIPE, text=True, stderr=subprocess.DEVNULL)
    command_output = process.stdout

    pattern = r"(/[\w\-./]+)\s+\(Status:\s+(\d+)\)"
    matches = re.findall(pattern, command_output)

    filtered_results = [{"path": match[0], "status": int(match[1])} for match in matches]

    return filtered_results



