import psutil
import time
import logging
from datetime import datetime

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80
LOG_FILE = "/var/log/system_health.log"

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

def get_memory_usage():
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    return memory_usage

def get_disk_usage():
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    return disk_usage

def get_running_processes():
    processes = len(psutil.pids())
    return processes

def check_thresholds():
    cpu = get_cpu_usage()
    memory = get_memory_usage()
    disk = get_disk_usage()
    processes = get_running_processes()

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if cpu > CPU_THRESHOLD:
        message = f"CPU usage is high: {cpu}%"
        logging.info(message)
        print(f"{timestamp}: {message}")

    if memory > MEMORY_THRESHOLD:
        message = f"Memory usage is high: {memory}%"
        logging.info(message)
        print(f"{timestamp}: {message}")

    if disk > DISK_THRESHOLD:
        message = f"Disk usage is high: {disk}%"
        logging.info(message)
        print(f"{timestamp}: {message}")

    message = f"Number of running processes: {processes}"
    logging.info(message)
    print(f"{timestamp}: {message}")

def main():
    while True:
        check_thresholds()
        time.sleep(1)

if __name__ == "__main__":
    main()
