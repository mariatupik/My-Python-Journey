import psutil
from datetime import datetime

def check_health():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage('C:/')
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = (
    f"[{timestamp}]\n"
    f"CPU Load: {cpu}%\n"
    f"RAM Usage: {mem}%\n"
    f"Disk Total: {disk.total / (1024**3):.2f} GB\n"
    f"Disk Used: {disk.used / (1024**3):.2f} GB ({disk.percent}%)"
)
    
    if cpu > 80 or mem > 90:
        log_entry += " - ПОПЕРЕДЖЕННЯ: Високе навантаження!"
    
    return log_entry

def save_report(data):
    with open("health_log.txt", "a", encoding="utf-8") as file:
        file.write(data + "\n")

if __name__ == "__main__":
    status = check_health()
    print(status)
    save_report(status)