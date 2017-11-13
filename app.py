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
from flask import request
from tiradadi import setBotUp
from telegram import Update
from settings import TELEGRAM_HOOK

update_queue, bot_instance = setBotUp()

@application.route('/'+TELEGRAM_HOOK, methods=['GET', 'POST'])
def webhook():
	if request.json:
		update_queue.put(Update.de_json(request.json, bot_instance))
	return ''

if __name__ == '__main__':
	from wsgiref.simple_server import make_server
	httpd = make_server('localhost', 8443, application)
    
	httpd.serve_forever()


