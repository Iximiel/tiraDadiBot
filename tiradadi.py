import logging
from threading import Thread
from settings import TELEGRAM_TOKEN, TELEGRAM_URL_HOOK
from queue import Queue
from telegram import Bot
from telegram.ext import Dispatcher, Updater, CommandHandler

from handlers import tiradadi

#set up del bot
def setBotUp():
	logging.basicConfig(level=logging.WARNING)
	#setta il token
	bot = Bot(TELEGRAM_TOKEN)
	update_queue = Queue()
	#setta il Dispatcher
	dp = Dispatcher(bot, update_queue)
	
	dp.add_handler(CommandHandler('tira', tiradadi, pass_args=True))
	
	bot.set_webhook(webhook_url=TELEGRAM_URL_HOOK)
	thread = Thread(target=dp.start, name='dispatcher')
	thread.start()
	return update_queue, bot