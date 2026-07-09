import platform
import socket
import time
from datetime import datetime

import psutil


def get_system_information():

    cpu = psutil.cpu_percent(interval=1)

    memory = psutil.virtual_memory()

    disk = psutil.disk_usage("/")

    hostname = socket.gethostname()

    operating_system = platform.system()

    release = platform.release()

    ip = socket.gethostbyname(hostname)

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cores = psutil.cpu_count()

    network = psutil.net_io_counters()

    uptime = round((time.time() - psutil.boot_time()) / 3600, 2)

    processes = []

    try:

        for process in psutil.process_iter(

            ['pid', 'name', 'cpu_percent', 'memory_percent']

        ):

            try:

                processes.append({

                    "pid": process.info["pid"],

                    "name": process.info["name"],

                    "cpu": round(process.info["cpu_percent"], 1),

                    "memory": round(process.info["memory_percent"], 2)

                })

            except Exception:

                continue

    except Exception:

        pass

    processes = sorted(

        processes,

        key=lambda x: x["cpu"],

        reverse=True

    )

    processes = processes[:15]

    return {

        "cpu": cpu,

        "memory": memory.percent,

        "disk": disk.percent,

        "hostname": hostname,

        "os": operating_system,

        "release": release,

        "ip": ip,

        "time": current_time,

        "cores": cores,

        "sent": round(network.bytes_sent / (1024 * 1024), 2),

        "received": round(network.bytes_recv / (1024 * 1024), 2),

        "uptime": uptime,

        "processes": processes

    }