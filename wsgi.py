from flask import Flask, request
from telegram import Update
import tiradady
from settings import TELEGRAM_TOKEN, OPENSHIFT_GEAR_DNS, OPENSHIFT_PYTHON_IP, OPENSHIFT_PYTHON_PORT

app = Flask(__name__)
#update_queue, bot_instance = tiradady.setup(webhook_url='https://{}/{}'.format(OPENSHIFT_GEAR_DNS,TELEGRAM_TOKEN))

@app.route('/')
def index():
	return "<par>I'm creating this to make a Telegram bot for my friends<br>and I'm actually enjoing it!!</par>"+TELEGRAM_TOKEN
'''
@app.route('/'+TELEGRAM_TOKEN)
def webhook():
	if request.json:
		update_queue.put(Update.de_json(request.json, bot_instance))
	return ''
	'''
if __name__ == '__main__':
	ip = OPENSHIFT_PYTHON_IP
	port = int(OPENSHIFT_PYTHON_PORT)
	app.run()#host = ip, port = port)
	