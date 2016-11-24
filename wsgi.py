#!/usr/bin/python
from os import path, environ
#linea per testare
virtenv = path.join(environ.get('OPENSHIFT_PYTHON_DIR','.'), 'virtenv')
#virtenv = environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
virtualenv = path.join(virtenv, 'bin/activate_this.py')

try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass
#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#

from myflaskBase import app as application
from myflaskBase import update_queue, bot_instance
from tiradadi import setBotUp

app = Flask(__name__)
update_queue, bot_instance = setBotUp()


if __name__ == '__main__':
	from wsgiref.simple_server import make_server
	httpd = make_server('localhost', 8443, application)
    
	httpd.serve_forever()


