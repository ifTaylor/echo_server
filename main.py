import subprocess
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

files_to_run = ['./py/server.py', './py/client.py']

for file in files_to_run:
    subprocess.Popen(['python', file], creationflags=subprocess.CREATE_NEW_CONSOLE)