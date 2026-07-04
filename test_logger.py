from bot.logging_config import setup_logger

logger = setup_logger()

logger.info("Trading bot started successfully.")
logger.warning("This is a sample warning.")
logger.error("This is a sample error.")