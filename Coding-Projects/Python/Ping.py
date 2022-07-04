import subprocess

ip = input("Enter the IP Address you want to ping: ")

command_output = subprocess.run(["ping", ip], capture_output=True).stdout.decode()

print(command_output)