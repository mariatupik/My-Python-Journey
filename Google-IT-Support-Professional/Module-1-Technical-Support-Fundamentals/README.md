# 🖥️ Hardware Diagnostic Tool

This script was developed as a practical application of the concepts learned in **Module 1: Technical Support Fundamentals** (Google IT Support Professional Certificate).

### Objective
To automate the collection of crucial hardware and system information, which is a standard procedure in IT Support and System Administration for troubleshooting and asset management.

### Features
* Retrieves OS architecture and version.
* Analyzes CPU model, cores, and current utilization.
* Calculates total, used, and available RAM in a human-readable format.
* Maps all storage drives and checks capacity, handling `PermissionError` exceptions for protected system partitions.
* Automatically exports the collected data into a clean `hardware_report.txt` log file.

### Built With (Tools & Technologies)
* **Python 3.x**: The core programming language used for scripting.
* **psutil (Process and System Utilities)**: A cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors).
* **Platform Module**: Used to access underlying platform’s identifying data (OS name, version, and architecture).

### How to Run
1. Install the required dependency:
   `pip install -r requirements.txt`
2. Run the diagnostic script:
   `python system_monitor.py`
3. Open the generated `hardware_report.txt` file to view your system details.