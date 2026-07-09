from flask import render_template

import config

from services.monitoring import get_system_information
from services.deployment import deploy_application
from services.logger import read_logs
from services.git_service import (
    get_latest_commit,
    get_current_branch,
)


def register_routes(app):

    # ===========================
    # HOME PAGE
    # ===========================

    @app.route("/")
    def home():

        system = get_system_information()

        return render_template(
            "index.html",
            hostname=system["hostname"],
            current_time=system["time"],
            branch=get_current_branch(),
            commit=get_latest_commit(),
        )

    # ===========================
    # DEPLOYMENT
    # ===========================

    @app.route("/deploy")
    def deploy():

        result = deploy_application()

        return render_template(
            "deploy.html",
            message=result,
            server=config.SERVER_NAME,
            ip=config.SERVER_IP,
            env=config.ENVIRONMENT,
            version=config.APP_VERSION,
        )

    # ===========================
    # SERVER STATUS
    # ===========================

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
            current_time=system["time"],
        )

    # ===========================
    # LOGS
    # ===========================

    @app.route("/logs")
    def logs():

        log_data = read_logs()

        return render_template(
            "log.html",
            logs=log_data,
        )