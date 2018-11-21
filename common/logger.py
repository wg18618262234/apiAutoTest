import logging


def logger(level, msg):
    LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
    DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"

    logging.basicConfig(level=logging.DEBUG, filename='../logs/my.log', format=LOG_FORMAT, datefmt=DATE_FORMAT)

    if 'debug' in level:
        logging.debug(msg)
    elif 'info' in level:
        logging.info(msg)
    elif 'warning' in level:
        logging.warning(msg)
    elif 'error' in level:
        logging.error(msg)
    elif 'critical' in level:
        logging.critical(msg)
    else:
        logging.debug('error type of log !')
        return False



if __name__ == '__main__':
    logger('debug','test')