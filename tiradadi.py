import logging
from threading import Thread
from settings import TELEGRAM_TOKEN, TELEGRAM_URL_HOOK
from queue import Queue
from telegram import Bot
from telegram.ext import Dispatcher, Updater, CommandHandler

from handlers import tiradadi ,d4, d6, d8, d10, d12, d20, d100

#set up del bot
def setBotUp():
	logging.basicConfig(level=logging.WARNING)
	#setta il token
	bot = Bot(TELEGRAM_TOKEN)
	update_queue = Queue()
	#setta il Dispatcher
	dp = Dispatcher(bot, update_queue)
	
	dp.add_handler(CommandHandler('tira', tiradadi, pass_args=True))
	dp.add_handler(CommandHandler('d4', d4))
	dp.add_handler(CommandHandler('d6', d6))
	dp.add_handler(CommandHandler('d8', d8))
	dp.add_handler(CommandHandler('d10', d10))
	dp.add_handler(CommandHandler('d12', d12))
	dp.add_handler(CommandHandler('d20', d20))
	dp.add_handler(CommandHandler('d%', d100))
	
	bot.set_webhook(webhook_url=TELEGRAM_URL_HOOK)
	thread = Thread(target=dp.start, name='dispatcher')
	thread.start()
	return update_queue, bot