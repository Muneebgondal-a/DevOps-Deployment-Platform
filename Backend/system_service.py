import subprocess


def run_command(command):

    try:

        output = subprocess.check_output(
            command,
            shell=True,
            text=True
        )

        return output

    except Exception as error:

        return str(error)