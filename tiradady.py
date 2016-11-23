import logging
from settings import TELEGRAM_TOKEN
from queue import Queue
from telegram import Bot
from telegram.ext import Dispatcher, Updater, MessageHandler

def setup(webhook_url=None):
	logging.basicConfig(level=logging.WARNING)
	#setta il token
	bot = Bot(TELEGRAM_TOKEN)
	update_queue = Queue()
	#setta il Dispatcher
	dp = Dispatcher(bot, update_queue)


	bot.set_webhook(webhook_url=webhook_url)
	thread = Thread(target=dp.start, name='dispatcher')
	thread.start()
	return update_queue, bot