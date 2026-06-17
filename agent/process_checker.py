import psutil
TARGET_PROCESSES = [
    "ssh",
    "docker",
    "python",
    "chrome"
]
running_processes = []
for process in psutil.process_iter(['name']):
    try:
        running_processes.append(process.info['name'])
    except:
        pass
for target in TARGET_PROCESSES:
    found = False
    for running in running_processes:
        if running and target.lower() in running.lower():
            found = True
            break
    if found:
        print(f"{target}: RUNNING")
    else:
        print(f"{target}: NOT RUNNING")
