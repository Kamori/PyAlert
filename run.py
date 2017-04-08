#!/usr/bin/env python3
import argparse
import os

from pyalert.subsystems.alert import process_handler as alert_handler
from pyalert.subsystems.gui import process_handler as gui_handler
from pyalert.utilities.config_handler import PyAlertConfig
from pyalert.utilities import pyalert_logger

DEFAULT_CONFIG = os.path.dirname(os.path.realpath(__file__)) + '/config.ini'

# Need to add an extra component to the CLI run.py, look here
PYALERT_COMPONENTS = {"gui": gui_handler,
                      "alert": alert_handler}


parser = argparse.ArgumentParser(description='Application handler for pyalert')
parser.add_argument('-c', '--config', action='store',
                    dest='config_file',
                    help='Config file for setting up pyalert',
                    default=DEFAULT_CONFIG)
parser.add_argument('pyalert_component', action='store',
                    help='Specify the pyalert component you want engage. ('
                         'EX: '
                         'gui)')
parser.add_argument('component_action', action='store',
                    help='Supply the action you want the component to '
                         'perform, (EX: restart)')


if __name__ == "__main__":
    args = parser.parse_args()

    try:
        PyAlertConfig('pyalert', args.config_file)
        pyalert_logger.info("config {0} loaded".format(args.config_file))
    except FileNotFoundError:
        _config_msg = "Config file not found: {conf}"
        pyalert_logger.critical(_config_msg.format(conf=args.config_file))
        raise SystemExit

    try:
        pyalert_logger.info('Attempting to {0} {1}'.format(
            args.component_action, args.pyalert_component))
        component = PYALERT_COMPONENTS[args.pyalert_component.lower()]
    except KeyError:
        _invalid_msg = 'Invalid PyAlert component provided: {invalid}'
        _available_msg = 'Available components: {avail}'
        _available_components = ', '.join(PYALERT_COMPONENTS.keys())
        pyalert_logger.critical(
            _invalid_msg.format(invalid=args.pyalert_component.lower()))
        pyalert_logger.critical(
            _available_msg.format(avail=_available_components))
        raise SystemExit

    component(args.component_action.lower(), arg_parse=args)




## PyAlert

## Easy way to turn common errors into alerts to your customers

## UDP input for unsecure method

## Api alerts

## based on input store predefined messages

## accept either email or user identifier <-- be dynamic

