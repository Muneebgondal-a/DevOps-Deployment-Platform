import subprocess


def run_command(command):

    try:

        output = subprocess.check_output(

            command,

            shell=True,

            text=True,

            stderr=subprocess.DEVNULL

        )

        return output.strip()

    except Exception:

        return None


def get_docker_information():

    docker = {

        "installed": False,

        "running": False,

        "version": "Not Installed",

        "images": [],

        "containers": []

    }

    version = run_command("docker --version")

    if version:

        docker["installed"] = True

        docker["version"] = version

    info = run_command("docker info")

    if info:

        docker["running"] = True

    if docker["running"]:

        images = run_command(

            'docker images --format "{{.Repository}}|{{.Tag}}|{{.Size}}"'

        )

        if images:

            for image in images.splitlines():

                parts = image.split("|")

                if len(parts) == 3:

                    docker["images"].append({

                        "repository": parts[0],

                        "tag": parts[1],

                        "size": parts[2]

                    })

        containers = run_command(

            'docker ps -a --format "{{.Names}}|{{.Status}}|{{.Image}}"'

        )

        if containers:

            for container in containers.splitlines():

                parts = container.split("|")

                if len(parts) == 3:

                    docker["containers"].append({

                        "name": parts[0],

                        "status": parts[1],

                        "image": parts[2]

                    })

    return docker