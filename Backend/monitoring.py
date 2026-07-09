import psutil
import platform
import socket
from datetime import datetime


def get_system_information():

    cpu = psutil.cpu_percent(interval=1)

    memory = psutil.virtual_memory()

    disk = psutil.disk_usage("/")

    hostname = socket.gethostname()

    operating_system = platform.system()

    release = platform.release()

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {

        "cpu": cpu,

        "memory": memory.percent,

        "disk": disk.percent,

        "hostname": hostname,

        "os": operating_system,

        "release": release,

        "time": current_time

    }