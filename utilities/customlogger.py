import logging
import os


class LoggerGen:
    @staticmethod
    def log_generator():
        logging.basicConfig(filename=".\\logs\\orangehrm_automation.log",
                            level=logging.INFO,
                            format="%(asctime)s : %(levelname)s : %(name)s : %(message)s",
                            datefmt="%Y-%m-%d %H:%M:%S", force=True

                            )
        logger = logging.getLogger()
        return logger
