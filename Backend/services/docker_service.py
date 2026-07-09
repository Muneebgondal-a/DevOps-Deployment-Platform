import subprocess


def run_command(command):

    try:

        output = subprocess.check_output(
            command,
            shell=True,
            text=True,
            stderr=subprocess.STDOUT
        )

        return output.strip()

    except subprocess.CalledProcessError as error:

        return error.output.strip()


def get_docker_information():

    docker = {

        "installed": False,

        "running": False,

        "version": "Not Installed",

        "images": [],

        "containers": []

    }

    version = run_command("docker --version")

    if "Docker version" in version:

        docker["installed"] = True

        docker["version"] = version

    info = run_command("docker info")

    if "Server Version" in info:

        docker["running"] = True

    if docker["running"]:

        image_output = run_command(
            'docker images --format "{{.Repository}}|{{.Tag}}|{{.Size}}"'
        )

        if image_output:

            for line in image_output.splitlines():

                parts = line.split("|")

                if len(parts) == 3:

                    docker["images"].append({

                        "repository": parts[0],

                        "tag": parts[1],

                        "size": parts[2]

                    })

        container_output = run_command(
            'docker ps -a --format "{{.Names}}|{{.Status}}|{{.Image}}"'
        )

        if container_output:

            for line in container_output.splitlines():

                parts = line.split("|")

                if len(parts) == 3:

                    docker["containers"].append({

                        "name": parts[0],

                        "status": parts[1],

                        "image": parts[2]

                    })

    return docker


def start_container(name):

    return run_command(f"docker start {name}")


def stop_container(name):

    return run_command(f"docker stop {name}")


def restart_container(name):

    return run_command(f"docker restart {name}")


def remove_container(name):

    return run_command(f"docker rm -f {name}")