import os
import sys
import logging
import psutil

logging.basicConfig(
    filename='server_status.log', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def check_server_status(server_ip):
    param = "-n" if sys.platform.startswith("win") else "-c"
    response = os.system(f"ping {param} 1 {server_ip} > /dev/null 2>&1" if not sys.platform.startswith("win") else f"ping {param} 1 {server_ip} > nul")
    
    if response == 0:
        logging.info(f"Server {server_ip} is UP.")
        return True
    else:
        logging.warning(f"Server {server_ip} is DOWN.")
        return False

def check_system_resources():
    cpu_percent = psutil.cpu_percent(interval=1)
    ram_percent = psutil.virtual_memory().percent

    if cpu_percent > 80 or ram_percent > 80:
        logging.warning(f"High resource usage detected - CPU: {cpu_percent}%, RAM: {ram_percent}%")
    else:
        logging.info(f"Resource usage is normal - CPU: {cpu_percent}%, RAM: {ram_percent}%")

def kill_frozen_process(process_name):
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'] and process_name.lower() in proc.info['name'].lower():
                pid = proc.info['pid']
                logging.warning(f"Found frozen process {process_name} (PID: {pid}). Sending SIGKILL...")
                os.kill(pid, 9) 
                logging.info(f"Process {process_name} (PID: {pid}) was successfully killed.")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
            continue
def extract_critical_errors():
    log_file = "server_status.log"
    error_file = "critical_errors.txt"
    if not os.path.exists(log_file):
        return
        
    logging.info("Running log analysis (Python-powered grep)...")
    
    with open(log_file, "r") as f:
        lines = f.readlines()
        
    critical_lines = [line for line in lines if "WARNING" in line or "ERROR" in line]

    if critical_lines:
        with open(error_file, "w") as ef:
            ef.writelines(critical_lines[-10:])
        logging.info(f"Extracted {len(critical_lines[-10:])} critical errors to {error_file}")

if __name__ == "__main__":
    logging.info("--- Monitoring Script Started ---")
    check_server_status("8.8.8.8")
    check_system_resources()
    kill_frozen_process("notepad")
    extract_critical_errors()
    logging.info("--- Monitoring Script Finished ---")