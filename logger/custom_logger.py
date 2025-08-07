from datetime import datetime
import logging
import os


class CustomLogger:
    """Custom logger class for the application."""

    def __init__(self, log_dir="logs"):
        """Initialise the CustomLogger class object with required objects and variables."""
        # ensure logs directory exists
        self.logs_dir = os.path.join(os.getcwd(), log_dir)
        os.makedirs(self.logs_dir, exist_ok=True)

        # create timestamped log file name
        LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
        log_file_path = os.path.join(self.logs_dir, LOG_FILE)

        # configure logging
        logging.basicConfig(
            filename=log_file_path,
            format="[ %(asctime)s ] %(levelname)s %(name)s (line:%(lineno)d) - %(message)s",
            level=logging.INFO,
        )

    def get_logger(self, name=__file__):
        return logging.getLogger(name=os.path.basename(name))


if __name__ == "__main__":
    logger = CustomLogger()
    logger = logger.get_logger(__file__)
    logger.info("Custom Logger is initialised")
