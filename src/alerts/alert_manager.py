from datetime import datetime

def send_alert(service, message, severity="INFO"):

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\n========== ALERT ==========")
    print(f"Time      : {current_time}")
    print(f"Service   : {service}")
    print(f"Severity  : {severity}")
    print(f"Message   : {message}")
    print("===========================\n")


if __name__ == "__main__":

    send_alert(
        "nginx-demo",
        "Container restarted successfully",
        "INFO"
    )
