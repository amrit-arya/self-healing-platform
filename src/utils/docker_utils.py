import subprocess

def list_running_containers():
    result = subprocess.run(
        ["docker", "ps", "--format", "{{.Names}}"],
        capture_output=True,
        text=True
    )
    return result.stdout.splitlines()

def start_container(container_name):
    subprocess.run(
        ["docker", "start", container_name],
        capture_output=True,
        text=True
    )

def stop_container(container_name):
    subprocess.run(
        ["docker", "stop", container_name],
        capture_output=True,
        text=True
    )
