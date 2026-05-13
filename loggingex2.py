import logging  
#log.basicConfig(filename='C:\\manilogs\\example.log', level=log.INFO)
# Configure logging with a specific format and timestamp
logging.basicConfig(
    filename='C:\\manilogs\\startup.log',      # Name of the file
    filemode='a',                # 'a' for append (default), 'w' for overwrite
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S', # Format for the timestamp
    level=logging.DEBUG          # Lowest level to capture (DEBUG, INFO, WARNING, ERROR, CRITICAL)
)

# Usage examples
logging.debug("This is a detailed debug message")
logging.info("Standard startup information")
logging.warning("Something unexpected happened")
logging.error("A serious error occurred")