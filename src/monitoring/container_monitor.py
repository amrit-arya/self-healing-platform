import subprocess

result = subprocess.run(
    ["docker", "ps", "--format", "{{.Names}}"],
    capture_output=True,
    text=True
)

containers = result.stdout.splitlines()

print("Running Containers:\n")

for container in containers:
    print(container)
