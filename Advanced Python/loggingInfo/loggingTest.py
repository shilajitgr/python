import logging

# logging.basicConfig(level=logging.DEBUG) # DEBUG is the lowest level of logging
# by default the logging module logs messages with level WARNING or higher
logging.basicConfig(filename="game.log", format="%(asctime)s-%(name)s-%(levelname)s-%(message)s",
                    datefmt="%m/%d/%Y %H:%M:%S", level=logging.DEBUG) # logs to a file

# if two lines of logging.basicConfig are written, the second one will have no effect

# following lines will not overwrite the log file, but will append to it
# if the file already exists

def logging_func():
    logger = logging.getLogger(__name__)
    
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")

logging_func()