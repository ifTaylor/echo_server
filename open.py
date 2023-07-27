import subprocess
import os

def run_script_in_console(script_path):
    process = subprocess.Popen(['python', script_path], creationflags=subprocess.CREATE_NEW_CONSOLE)
    return str(process.pid)

def run(files_to_run):
    with open('running_scripts.txt', 'w') as pid_file:
        for file in files_to_run:
            pid = run_script_in_console(file)
            pid_file.write(pid + '\n') 

def main():
    files_to_run = [
        './py/server.py',
        './py/client.py'
    ]

    run(files_to_run)

if __name__ == "__main__":
    main()