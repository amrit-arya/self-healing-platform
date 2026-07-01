import subprocess
import time

CHECK_INTERVAL = 30

print("Starting Self-Healing Monitor...")

while True:

    print("\nRunning health check...\n")

    subprocess.run(
        ["python", "-m", "recovery.auto_recovery"]
    )

    print(f"Sleeping for {CHECK_INTERVAL} seconds...\n")

    time.sleep(CHECK_INTERVAL)
