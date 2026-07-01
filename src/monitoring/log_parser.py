from pathlib import Path
# Get project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Path to log file
LOG_FILE = PROJECT_ROOT / "logs" / "application.log"

# Path to report file
REPORT_FILE = PROJECT_ROOT / "reports" / "log_report.txt"

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
