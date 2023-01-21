import logging, datetime

_log_name = f"""logs/{datetime.datetime.now().strftime("%d-%m-%y %H-%M-%S")}.log"""
_log_format = f"%(levelname)s %(asctime)s %(message)s (File: %(filename)s) (Function: %(funcName)s (Line: %(lineno)d))"
_datefmt = f"%d/%m/%Y %H:%M:%S"


def get_file_handler():
    file_handler = logging.FileHandler("logs/example.log")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(_log_format, _datefmt))
    return file_handler

def get_stream_handler():
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter(_log_format, _datefmt))
    return stream_handler

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(get_file_handler())
    logger.addHandler(get_stream_handler())
    return logger