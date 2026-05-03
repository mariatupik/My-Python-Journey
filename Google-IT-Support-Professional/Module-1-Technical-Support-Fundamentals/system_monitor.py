# Connecting "tools" (Import)
import platform
import psutil
import datetime

# Byte conversion function (get_size)

def get_size(bytes_size, suffix="B"):
    """Converts bytes to a human-readable format (e.g., MB, GB)."""
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes_size < factor:
            return f"{bytes_size:.2f} {unit}{suffix}"
        bytes_size /= factor

def generate_system_report():
    report_lines = []
    
    # 1. Header with Timestamp
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_lines.append("=" * 40)
    report_lines.append(" SYSTEM HARDWARE DIAGNOSTIC REPORT ")
    report_lines.append("=" * 40)
    report_lines.append(f"Generated on: {current_time}\n")

    # 2. Operating System Info
    report_lines.append("[+] OPERATING SYSTEM:")
    report_lines.append(f"    System: {platform.system()} {platform.release()}")
    report_lines.append(f"    Architecture: {platform.machine()}\n")

    # 3. CPU Info
    report_lines.append("[+] PROCESSOR (CPU):")
    report_lines.append(f"    Model: {platform.processor()}")
    report_lines.append(f"    Physical Cores: {psutil.cpu_count(logical=False)}")
    report_lines.append(f"    Total Threads: {psutil.cpu_count(logical=True)}")
    report_lines.append(f"    Current Utilization: {psutil.cpu_percent(interval=1)}%\n")

    # 4. RAM Info
    report_lines.append("[+] MEMORY (RAM):")
    virtual_mem = psutil.virtual_memory()
    report_lines.append(f"    Total RAM: {get_size(virtual_mem.total)}")
    report_lines.append(f"    Available RAM: {get_size(virtual_mem.available)}")
    report_lines.append(f"    Used RAM: {get_size(virtual_mem.used)} ({virtual_mem.percent}%)\n")

    # 5. Disk Space Info
    report_lines.append("[+] DISK STORAGE:")
    partitions = psutil.disk_partitions()
    for partition in partitions:
        report_lines.append(f"    Drive: {partition.device} ({partition.fstype})")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
            report_lines.append(f"      Total Size: {get_size(partition_usage.total)}")
            report_lines.append(f"      Free Space: {get_size(partition_usage.free)}")
            report_lines.append(f"      Used Space: {partition_usage.percent}%")
        except PermissionError:
            # Catching permission errors for restricted system drives
            report_lines.append("      Status: Permission Denied (System Protected)")
        report_lines.append("")

    # 6. Write to File
    filename = "hardware_report.txt"
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("\n".join(report_lines))
        print(f"✅ Success! System report has been saved to '{filename}'.")
    except Exception as e:
        print(f"❌ Error saving report: {e}")

if __name__ == "__main__":
    generate_system_report()