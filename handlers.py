from random import randint

def dado(num):
	return randint(1,num)
	
def example_handler(bot, update):
	# Remove this handler
	bot.send_message(
		update.message.chat_id,
		text='Hello from openshift'
	)
'''
def example_handler(bot, update):
	# Remove this handler
	#update.message.reply_text('Hello from openshift! ' + str(dado(10)))
'''
# Write your handlers here

def tiradedi(bot,update,args):
	for arg in args:
		bot.send_message(chat_id=update.message.chat_id, text=str(arg))
        bot.send_message(chat_id=update.message.chat_id, text=type(arg))
	#update.message.reply_text('Hello from openshift! ' + str(dado(10)))

	
def tiradadi(bot,update,args):
	if not args:
		update.message.reply_text("lancia n dadi di tipo x, puoi aggiungere o togliere y: /tira ndx+y")
	else:
		for arg in args:
			toreturn ='"'+ arg +'"'
			if "d" in arg:
				N = 0 #numero di dadi da lanciare
				D = 0 #tipo di dado
				MP = 0 #bonus positivi
				MM = 0 #malus
				#procedo col dividere la sintassi del tiro di dado
				n,dice = arg.split("d")
				#controllo se ci sono malus/bonus
				if "+" in dice:
					tmp, modpl = dice.split("+")
					dice = tmp
					MP = int(modpl)
				
				if "-" in dice:
					tmp, modmin = dice.split("-")
					dice = tmp
					MM = int(modmin)
				
				N = int(n)
				D = int(dice)
				tot = 0
				if N == 1:
					tot = dado(D)
					toreturn += ": "+ str(tot)
				else :
					text = ""
					while N>0:
						tiro = dado(D)
						tot += tiro
						text+= " " + str(tiro)
						N-=1
						
					toreturn += ":"+ text + "\ntot: "+ str(tot)
					
				if MP>0:
					toreturn+=" + " + str(MP) + " = " + str(tot+MP)
				if MM>0:
					toreturn+=" - " + str(MM) + " = " + str(tot-MM)

			else:
				toreturn+=": sintassi errata, ricordati di usare d minuscolo!!!"	
				
			update.message.reply_text(toreturn)