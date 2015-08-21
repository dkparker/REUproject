import subprocess

with open("configs2.txt", 'r') as configs:
    for line in configs:
        line = line[:-1]
        subprocess.call(["./btest", "--codes-config="+line])
