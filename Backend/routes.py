from flask import render_template, redirect, request, url_for
from flask_login import login_user, logout_user, login_required, current_user

import config

from auth import User, validate_user

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
    # LOGIN
    # ==========================================

    @app.route("/login", methods=["GET", "POST"])
    def login():

        if current_user.is_authenticated:
            return redirect(url_for("home"))

        if request.method == "POST":

            username = request.form.get("username")
            password = request.form.get("password")

            if validate_user(username, password):

                user = User(username)

                login_user(user)

                return redirect(url_for("home"))

            return render_template(
                "login.html",
                error="Invalid Username or Password"
            )

        return render_template("login.html")

    # ==========================================
    # LOGOUT
    # ==========================================

    @app.route("/logout")
    @login_required
    def logout():

        logout_user()

        return redirect(url_for("login"))

    # ==========================================
    # HOME
    # ==========================================

    @app.route("/")
    @login_required
    def home():

        system = get_system_information()

        return render_template(

            "index.html",

            hostname=system["hostname"],

            current_time=system["time"],

            branch=get_current_branch(),

            commit=get_latest_commit(),

            username=current_user.id,

        )

    # ==========================================
    # STATUS
    # ==========================================

    @app.route("/status")
    @login_required
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
    @login_required
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
    @login_required
    def logs():

        return render_template(

            "log.html",

            logs=read_logs(),

        )

    # ==========================================
    # DOCKER DASHBOARD
    # ==========================================

    @app.route("/docker")
    @login_required
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
    @login_required
    def docker_start(name):

        start_container(name)

        return redirect("/docker")

    # ==========================================
    # STOP CONTAINER
    # ==========================================

    @app.route("/docker/stop/<name>")
    @login_required
    def docker_stop(name):

        stop_container(name)

        return redirect("/docker")

    # ==========================================
    # RESTART CONTAINER
    # ==========================================

    @app.route("/docker/restart/<name>")
    @login_required
    def docker_restart(name):

        restart_container(name)

        return redirect("/docker")

    # ==========================================
    # REMOVE CONTAINER
    # ==========================================

    @app.route("/docker/remove/<name>")
    @login_required
    def docker_remove(name):

        remove_container(name)

        return redirect("/docker")