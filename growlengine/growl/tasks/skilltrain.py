import logging
import rollbar
from celery import task

logger = logging.getLogger(__name__)

@task()
def task_skill_train():
    logger.debug('Training skills...')
    rollbar.report_message('trained a skill')
    logger.debug('Skills trained!')