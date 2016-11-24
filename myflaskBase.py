from flask import Flask
from settings import TELEGRAM_HOOK
from telegram import Update

app = Flask(__name__)
'''
from tiradadi import setBotUp
update_queue, bot_instance = setBotUp()
'''

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