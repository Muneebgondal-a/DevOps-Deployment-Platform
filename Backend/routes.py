from flask import render_template

import config
from monitoring import get_system_information
from deployment import deploy_application
from logger import read_logs
from git_service import get_latest_commit, get_current_branch


def register_routes(app):

    # ================= HOME =================

    @app.route("/")
    def home():

        system = get_system_information()

        return render_template(
            "index.html",
            branch=get_current_branch(),
            commit=get_latest_commit(),
            hostname=system["hostname"],
            current_time=system["time"]
        )

    # ================= DEPLOY =================

    @app.route("/deploy")
    def deploy():

        result = deploy_application()

        return render_template(
            "deploy.html",
            message=result,
            server=config.SERVER_NAME,
            ip=config.SERVER_IP,
            env=config.ENVIRONMENT,
            version=config.APP_VERSION
        )

    # ================= STATUS =================

    @app.route("/status")
    def status():

        system = get_system_information()

        return render_template(
            "status.html",
            cpu=system["cpu"],
            memory=system["memory"],
            disk=system["disk"],
            hostname=system["hostname"],
            os=system["os"],
            release=system["release"],
            current_time=system["time"]
        )

    # ================= LOGS =================

    @app.route("/logs")
    def logs():

        log_data = read_logs()

        return render_template(
            "logs.html",
            logs=log_data
        )