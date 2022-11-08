import inspect
import logging
import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:
    def get_logging(self):
        logger_name = inspect.stack()[0][3]
        log = logging.getLogger(logger_name)
        file_handler = logging.FileHandler("logs.log")  # responsible for calling package
        log.addHandler(file_handler)
        set_format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(set_format)
        log.setLevel(logging.INFO)  # sets only the logs that contain info
        # log.debug("This is debug statement")
        # log.info("This info statement")
        # log.debug("This is debug statement")
        # log.critical("This is critical statement")
        # log.error("This is error statement")
        # log.warning("This is warning statement")
        return log

