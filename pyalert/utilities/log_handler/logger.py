import logging

def get_pyalert_logger():
    pyalert_logger = logging.getLogger('pyalert')
    pyalert_logger.setLevel(logging.INFO)

    stream = logging.StreamHandler()
    stream.setLevel(logging.INFO)

    #log_format = logging.Formatter('[%(asctime)s:%(filename)s:%(lineno)s - %('
    #                               'funcName)20s()] %(levelname)s: %(
    ## message)s'
    #                                '%Y-%m-%d %H:%M:%S')
    log_format = logging.Formatter('[%(asctime)s:%(filename)s:%(lineno)s - %('
                                   'funcName)10s()] %(levelname)s: %('
                                   'message)s', '%Y-%m-%d %H:%M:%S')
    stream.setFormatter(log_format)

    pyalert_logger.addHandler(stream)

    return pyalert_logger