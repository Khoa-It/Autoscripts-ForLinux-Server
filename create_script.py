import subprocess
filename = input("Enter file name: ")
if not filename:
    exit()

subprocess.run(["touch",filename])
subprocess.run(["chmod","777",filename])
