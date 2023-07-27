import os

def kill_processes_from_file(file_path):
    with open(file_path, 'r') as pid_file:
        pids = [int(pid.strip()) for pid in pid_file.readlines()]

    for pid in pids:
        try:
            os.kill(pid, 9)
        except OSError:
            pass

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'running_scripts.txt')
    kill_processes_from_file(file_path)

if __name__ == "__main__":
    main()
