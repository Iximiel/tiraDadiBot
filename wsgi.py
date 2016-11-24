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
'''
#from myflaskBase import app as application
#from myflaskBase import update_queue, bot_instance
from tiradadi import setBotUp

update_queue, bot_instance = setBotUp()


if __name__ == '__main__':
	from wsgiref.simple_server import make_server
	httpd = make_server('localhost', 8443, application)
    
	httpd.serve_forever()


'''
from flask import Flask
from settings import TELEGRAM_HOOK
from telegram import Update

app = Flask(__name__)

from tiradadi import setBotUp
update_queue, bot_instance = setBotUp()


@app.route('/')
def explanation():
	return "<par>I'm creating this to make a Telegram bot for my friends<br>and I'm actually enjoing it(more or <b>less<\b>)!!</par>"
	
@app.route('/'+TELEGRAM_HOOK)
def webhook():
	if request.json:
		update_queue.put(Update.de_json(request.json, bot_instance))
	return ''
	
if __name__ == '__main__':
	app.run()