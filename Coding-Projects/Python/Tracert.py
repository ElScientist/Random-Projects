import subprocess

ip = input("Enter the IP Address you want to trace: ")

command_output = subprocess.run(["tracert", ip], capture_output=True).stdout.decode()

print(command_output)