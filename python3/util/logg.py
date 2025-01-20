'''
demo how the logger works
'''

from loguru import logger

# Configure Loguru to write logs to a file
logger.add("my_app.log", rotation="10MB", retention="7 days", level="DEBUG")

# Example usage
logger.debug("This is a debug message")
logger.info("This is an informational message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
