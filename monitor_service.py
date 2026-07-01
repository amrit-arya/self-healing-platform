import subprocess
import time

from src.config.settings import CHECK_INTERVAL

print("Starting Self-Healing Monitor...")

while True:

    print("\nRunning health check...\n")

    subprocess.run(
        ["python", "-m", "recovery.auto_recovery"]
    )

    print(f"Sleeping for {CHECK_INTERVAL} seconds...\n")

    time.sleep(CHECK_INTERVAL)
