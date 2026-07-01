from pathlib import Path
from src.config.paths import LOGS_DIR, REPORTS_DIR

LOG_FILE = LOGS_DIR / "application.log"
REPORT_FILE = REPORTS_DIR / "log_report.txt"

errors = []
warnings = []

with open(LOG_FILE, "r") as file:

    for line in file:

        if "ERROR" in line:
            errors.append(line.strip())

        if "WARNING" in line:
            warnings.append(line.strip())

print("\nERRORS")

for error in errors:
    print(error)

print("\nWARNINGS")

for warning in warnings:
    print(warning)

print(f"\nTotal Errors: {len(errors)}")
print(f"Total Warnings: {len(warnings)}")

with open(REPORT_FILE, "w") as report:

    report.write(f"Errors: {len(errors)}\n")
    report.write(f"Warnings: {len(warnings)}\n")

print("\nReport generated successfully.")
