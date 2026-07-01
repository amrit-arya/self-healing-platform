import subprocess
from datetime import datetime
from alerts.alert_manager import send_alert
from pathlib import Path

from src.config.paths import LOGS_DIR, REPORTS_DIR

LOG_FILE = LOGS_DIR / "application.log"
REPORT_FILE = REPORTS_DIR / "log_report.txt"


# Containers that must always be running
from src.config.settings import REQUIRED_CONTAINERS

print("\n========== SELF HEALING ENGINE ==========\n")

# Get list of running containers
result = subprocess.run(
    ["docker", "ps", "--format", "{{.Names}}"],
    capture_output=True,
    text=True
)

running_containers = result.stdout.splitlines()

for container in REQUIRED_CONTAINERS:

    print(f"\nChecking: {container}")

    # Container is healthy
    if container in running_containers:

        print(f"Status: RUNNING")

    # Container is down
    else:

        print(f"Status: STOPPED")
        print("Attempting recovery...")

        # Start container
        subprocess.run(
            ["docker", "start", container],
            capture_output=True,
            text=True
        )

        # Verify recovery
        verify = subprocess.run(
            ["docker", "ps", "--format", "{{.Names}}"],
            capture_output=True,
            text=True
        )

        running_after_recovery = verify.stdout.splitlines()

        if container in running_after_recovery:

            print(f"Recovery Status: SUCCESS")

            # Create incident report
            with open(INCIDENTS_FILE, "a") as report:

                report.write(
                    f"{datetime.now()} | "
                    f"{container} crashed | "
                    f"Recovered automatically\n"
                )

            send_alert(
    container,
    "Container recovered successfully",
    "INFO"
)

        else:

            send_alert(
    container,
    "Automatic recovery failed",
    "CRITICAL"
)

            with open(INCIDENTS_FILE, "a") as report:

                report.write(
                    f"{datetime.now()} | "
                    f"{container} crashed | "
                    f"Recovery failed\n"
                )

            print("Failure recorded in incident report.")

print("\n========== RECOVERY CHECK COMPLETE ==========\n")
