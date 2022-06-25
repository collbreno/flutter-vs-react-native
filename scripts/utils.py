import subprocess

def syscall(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)
