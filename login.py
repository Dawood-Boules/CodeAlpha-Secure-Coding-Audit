import subprocess

username = input("Enter your username: ")
subprocess.call(f"echo Hello {username}", shell=True)
