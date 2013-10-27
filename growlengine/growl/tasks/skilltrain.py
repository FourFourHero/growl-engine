import logging
from celery import task

logger = logging.getLogger(__name__)

@task()
def task_skill_train():
    logger.debug('Training skills...')

    logger.debug('Skills trained!')