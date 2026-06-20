log_file = "../logs/application.log"

errors = []
warnings = []

with open(log_file, "r") as file:

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

report_file = "../reports/log_report.txt"

with open(report_file, "w") as report:

    report.write(f"Errors: {len(errors)}\n")
    report.write(f"Warnings: {len(warnings)}\n")

print("\nReport generated successfully.")
