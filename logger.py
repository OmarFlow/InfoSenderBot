import logging
import sys

logger = logging.getLogger('logger')

logger.setLevel(logging.ERROR)
consoleHandler = logging.StreamHandler(sys.stdout)
logger.addHandler(consoleHandler)