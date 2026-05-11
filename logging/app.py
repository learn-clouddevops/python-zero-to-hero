import logging


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger=logging.getLogger("AirthemeticApp")


def add(a,b):
    logger.debug(f"Adding {a} and {b}")
    return a + b

def subtract(a,b):
    logger.debug(f"Subtracting {b} from {a}")
    return a - b
def multiply(a,b):
    logger.debug(f"Multiplying {a} and {b}")
    return a * b    

def divide(a,b):
    logger.debug(f"Dividing {a} by {b}")
    if b == 0:
        logger.error("Division by zero is not allowed")
        return None
    return a / b


add(10,15)
subtract(20,5)
multiply(4,6)
divide(10,2)
divide(10,0)
