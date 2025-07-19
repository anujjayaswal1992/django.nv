# vuln_example.py

import os
import subprocess

def insecure_command(user_input):
    # Dangerous: vulnerable to command injection
    os.system("echo " + user_input)

def another_insecure_command(user_input):
    # Also dangerous: uses shell=True with untrusted input
    subprocess.run(f"ls {user_input}", shell=True)

def hardcoded_secret():
    # Hardcoded secret (for testing secret detection)
    password = "supersecret123"
    return password

def use_eval():
    # Dangerous: using eval on user input
    eval(user_input)
