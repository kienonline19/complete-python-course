import logging

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s", 
    datefmt='%d/%m/%Y %H:%M:%S',
    level=logging.DEBUG,
    filename="logs.txt"
)

logger = logging.getLogger('books')

logger.debug("This is a debug message.")
logger.info("This will not show up.")
logger.warning("This will.")
logger.critical("This is a critical message.")

logger = logging.getLogger('books.database')

