import logging

logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler("game.log")

stream_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR)

formatter = logging.Formatter("%(name)s-%(levelname)s-%(message)s")

stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.warning("This is a warning message")
logger.error("This is an error message")

# instead of configuring the handlers and formatters for each logger, in the code
# a logging.conf file can be created with all the details
# and then the logging module can be configured to use that file like so

# logging.config.fileConfig("logging.conf") # this will accept the conf format listed below
# logging.config.dictConfig("logging.conf") # this will accept a dictionary format

# the logging.conf file will look like this:
"""
[loggers]
keys=root, exampleLogger

[handlers]
keys=consoleHandler, fileHandler

[formatters]
keys=sampleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler, fileHandler

[logger_exampleLogger]
level=DEBUG
handlers=consoleHandler
qualname=exampleLogger
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=sampleFormatter
args=(sys.stdout,)

[handler_fileHandler]
class=FileHandler
level=ERROR
formatter=sampleFormatter
args=("example.log",)

[formatter_sampleFormatter]
format=%(asctime)s-%(name)s-%(levelname)s-%(message)s
datefmt=%m/%d/%Y %H:%M:%S
"""