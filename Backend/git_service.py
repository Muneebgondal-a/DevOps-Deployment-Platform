import subprocess


def get_latest_commit():

    try:

        commit = subprocess.check_output(
            ["git", "log", "-1", "--pretty=%B"],
            text=True
        ).strip()

        return commit

    except Exception:

        return "Git repository not found."


def get_current_branch():

    try:

        branch = subprocess.check_output(
            ["git", "branch", "--show-current"],
            text=True
        ).strip()

        return branch

    except Exception:

        return "Unknown"