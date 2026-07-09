from services.logger import logger
from services.history import save_deployment


def deploy_application():

    logger.info("Deployment Started")

    save_deployment()

    logger.info("Deployment Finished")

    return "Deployment Successful"