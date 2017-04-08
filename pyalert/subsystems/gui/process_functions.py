from pyalert.utilities.config_handler import PyAlertConfig
from .application import configure
def process_start():
    gui_config = PyAlertConfig.get_config()['pyalert']
    if gui_config.getboolean('gui', 'use_flask_builtin_server'):
        app = configure(debug=gui_config.getboolean('gui', 'debug'))
        app.threaded = gui_config.getboolean('gui', 'threaded')
        app.run(host=gui_config.get('gui', 'listen'), port=gui_config.get(
            'gui', 'port'))
    else:
        return configure(debug=gui_config.getboolean('gui', 'debug'))

def process_shutdown():
    raise NotImplementedError('API shutdown currently not implemented')

def process_restart():
    raise NotImplementedError('API restart currently not implemented')