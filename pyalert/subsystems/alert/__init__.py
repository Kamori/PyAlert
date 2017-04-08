from pyalert.subsystems.alert.process_functions import (
    process_start, process_shutdown, process_restart)
from pyalert.utilities import pyalert_logger
from pyalert.utilities.exceptions import InvalidAction

import traceback

## initialization handler for pyalert alert subsystem


AVAILABLE_ACTIONS = {"start": process_start,
                     "shutdown": process_shutdown,
                     "restart": process_restart}

def process_handler(action, config=None, arg_parse=None):
    try:
        # If we catch keyerrors here we catch them everywhere
        if action not in AVAILABLE_ACTIONS:
            raise InvalidAction

        AVAILABLE_ACTIONS[action]()
        pyalert_logger.info('alert subsystem has successfully {0}'.format(
            action))
    except InvalidAction:
        pyalert_logger.critical('Invalid alert action: {0}'.format(action))
        pyalert_logger.critical('Available alert actions: {0}'.format(
            ', '.join(AVAILABLE_ACTIONS.keys())))
    except Exception as e:
        trace = traceback.format_exc()
        pyalert_logger.critical('Failed to {0} alert'.format(action))
        pyalert_logger.critical(trace)
        pyalert_logger.critical(e)