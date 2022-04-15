import logging
class LogGen:
    @staticmethod
    def logger(self):
        logging.basicConfig(filename=".\\Logs\\automation.log",
                        format='%(asctime)s: %(levelname)s: %(message)s:', datefmt='%m/%d/%y%I:%M:%S %P')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger