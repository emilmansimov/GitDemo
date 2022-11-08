from pytestDemo.BaseClass import BaseClass


class TestLoggingDemo(BaseClass):

    def test_logDemo(self):
        logger = BaseClass.get_logging(self)
        balance = 2000
        balance1 = 5000
        if balance >= balance1:
            logger.info("Numbers don't match")
        elif balance < balance1:
            logger.error("Balance is below the minimum requirement")

