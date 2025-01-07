import logging
import traceback
try:
    a = [1, 2, 3]
    val = a[4]
    
except IndexError as e:
    logging.error(e)    # this will only print the errot
    logging.error(e, exc_info=True)    # this will print the error and the stack trace

except Exception:
    logging.error("The error is: {0}".format(traceback.format_exc())) 
    # this will print stack trace even when the error is not encapsulated in a variable