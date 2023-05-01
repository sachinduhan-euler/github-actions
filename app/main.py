import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
)

LOGGER = logging.getLogger(__package__)

def hello():
    LOGGER.info("Hello world")
    return True