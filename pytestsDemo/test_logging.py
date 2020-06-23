import logging

def test_logging():
    logger = logging.getLogger(__name__)
    filehandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s: %(levelname)s :%(name)s : %(message)s")
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)   #filehandler object
    logger.setLevel(logging.INFO)
    logger.debug("Debug statement")
    logger.info("Information statement")
    logger.warning("Warning Statement")
    logger.error("Error statement")
    logger.critical("Critical statment")