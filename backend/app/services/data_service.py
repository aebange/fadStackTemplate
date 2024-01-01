import logging

logger = logging.getLogger('flaskLogger')


# data_service.py
def get_data():
    # Your logic to fetch or process data goes here
    data = {'message': 'Hello from Flask!'}
    logger.debug("Hello!")
    return data
