import logging
logging.basicConfig(filename='log.txt',level=logging.INFO)
logging.info("A new request come")
try:
    x=int(input("Enter first input number:"))
    y=int(input("Enter second input number:"))
    print(x/y)
except ZeroDivisionError as msg:
    print("We cannot divide with zero")
    logging.exception(msg)
except ValueError as msg:
    print("Only int value will be accepted")
    logging.exception(msg)
logging.info("Request processing completed")