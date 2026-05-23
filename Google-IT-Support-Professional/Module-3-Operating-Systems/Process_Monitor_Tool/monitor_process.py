import psutil
import time
from datetime import datetime

LimitCpu = 50.0
LimitRam = 500.0

def MonitorProcesses():
    print(f"Monitoring Started At {datetime.now()}")
    
    with open("ProcessLog.txt", "a", encoding="utf-8") as LogFile:
        for Process in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
            try:
                Name = Process.info['name']
                Pid = Process.info['pid']
                Cpu = Process.info['cpu_percent']
                
                MemoryInfo = Process.info['memory_info']
                Ram = MemoryInfo.rss / (1024 * 1024) if MemoryInfo else 0.0
                
                if Cpu > LimitCpu or Ram > LimitRam:
                    LogEntry = f"{datetime.now()} | Alert: Process '{Name}' (Pid: {Pid}) Is Using {Cpu}% Cpu And {Ram:.2f} Mb Ram\n"
                    LogFile.write(LogEntry)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue

if __name__ == "__main__":
    while True:
        MonitorProcesses()
        time.sleep(60)