# from pytestDemo.BaseClass import BaseClass
#
#
# class TestLogging(BaseClass):
#
#     def test_logDemo(self):
#         logger = BaseClass.get_logging(self)
#         balance = 2000
#         balance1 = 5000
#         if balance >= balance1:
#             logger.info("Numbers don't match")
#         elif balance < balance1:
#             assert logger.error("Balance is below the minimum requirement")
#_______________________________________________________________________________________________________________
#
# import logging
#
# def test_get_logging():
#     log = logging.getLogger(__name__)
#     file_handler = logging.FileHandler("logs.log")
#     log.addHandler(file_handler)
#     set_format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
#     file_handler.setFormatter(set_format)
#     log.setLevel(logging)
#     log.debug("This is debug statement")
#     log.info("This is info statement")
#     log.warning("This is warning statement")
#     log.error("This is error statement")
#     log.critical("This is critical statement")
from pytestDemo.BaseClass import BaseClass


class TestLogging(BaseClass):

    def test_log(self):
        logger = BaseClass.get_logging(self)
        balance = 2000
        balance1 = 5000
        if balance >= balance1:
            logger.info("Numbers do match")
        elif balance < balance1:
            assert logger.error("Balance is a below minimum requirement")

