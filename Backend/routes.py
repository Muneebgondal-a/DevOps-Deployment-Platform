from flask import render_template, redirect

import config

from services.monitoring import get_system_information
from services.deployment import deploy_application
from services.logger import read_logs
from services.git_service import (
    get_latest_commit,
    get_current_branch,
)

from services.docker_service import (
    get_docker_information,
    start_container,
    stop_container,
    restart_container,
    remove_container,
)


def register_routes(app):

    # ==========================================
    # HOME
    # ==========================================

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

    # ==========================================
    # STATUS
    # ==========================================

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

            ip=system["ip"],

            current_time=system["time"],

            cores=system["cores"],

            sent=system["sent"],

            received=system["received"],

            uptime=system["uptime"],

            processes=system["processes"],

        )

    # ==========================================
    # DEPLOY
    # ==========================================

    @app.route("/deploy")
    def deploy():

        message = deploy_application()

        return render_template(

            "deploy.html",

            message=message,

            server=config.SERVER_NAME,

            ip=config.SERVER_IP,

            env=config.ENVIRONMENT,

            version=config.APP_VERSION,

        )

    # ==========================================
    # LOGS
    # ==========================================

    @app.route("/logs")
    def logs():

        return render_template(

            "log.html",

            logs=read_logs(),

        )

    # ==========================================
    # DOCKER DASHBOARD
    # ==========================================

    @app.route("/docker")
    def docker():

        docker = get_docker_information()

        return render_template(

            "docker.html",

            docker=docker,

        )

    # ==========================================
    # START CONTAINER
    # ==========================================

    @app.route("/docker/start/<name>")
    def docker_start(name):

        start_container(name)

        return redirect("/docker")

    # ==========================================
    # STOP CONTAINER
    # ==========================================

    @app.route("/docker/stop/<name>")
    def docker_stop(name):

        stop_container(name)

        return redirect("/docker")

    # ==========================================
    # RESTART CONTAINER
    # ==========================================

    @app.route("/docker/restart/<name>")
    def docker_restart(name):

        restart_container(name)

        return redirect("/docker")

    # ==========================================
    # REMOVE CONTAINER
    # ==========================================

    @app.route("/docker/remove/<name>")
    def docker_remove(name):

        remove_container(name)

        return redirect("/docker")