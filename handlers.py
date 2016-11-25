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

def argbychar(arg,mychar):
	toreturn = ""
	N = 0 #numero di dadi da lanciare
	D = 0 #tipo di dado
	MP = 0 #bonus positivi
	MM = 0 #malus
	#procedo col dividere la sintassi del tiro di dado
	n,dice = arg.split(mychar,1)
	if not n:
		n = '1'#se non c'e` n prova a lanciare un dado dingolo
	if not n.isdigit():
		return ": sintassi errata"
	#controllo se ci sono malus/bonus
	if "+" in dice:
		tmp, modpl = dice.split("+")
		dice = tmp
		if not modpl.isdigit():
			return ": sintassi errata"
		MP = int(modpl)
	
	if "-" in dice:
		tmp, modmin = dice.split("-")
		dice = tmp
		if not modmin.isdigit():
			return ": sintassi errata"
		MM = int(modmin)
	
	N = int(n)
	if N>1000:
		return ": tira meno dadi!"
		
	if dice == '%':
		dice = '100'
	
	if not dice.isdigit():
			return ": sintassi errata"
	D = int(dice)
	
	if D>500:
		return ": tira dadi meno grossi, o devi proprio compensare?"
		
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
			
		toreturn += ":"+ text + "\n\ttot: "+ str(tot)
		
	if MP>0:
		toreturn+=" + " + str(MP) + " = " + str(tot+MP)
	if MM>0:
		toreturn+=" - " + str(MM) + " = " + str(tot-MM)
	return toreturn
	
 
def tiradadi(bot,update,args):
	message = ''
	if not args:
		message = "lancia n dadi di tipo x, puoi aggiungere o togliere y: /tira ndx+y puoi scrivere più espressioni differenti, separate da uno spazio"
	else:
		primo = True
		for arg in args:
			toreturn = ''
			if primo:
				primo=False
			else:
				toreturn += '\n'
			toreturn +='"'+ arg +'"'
			if "d" in arg:
				toreturn+=argbychar(arg,'d')
			elif "D" in arg:
				toreturn+=argbychar(arg,'D')
			else:
				toreturn+=": sintassi errata"
			
			message+=toreturn
	#print(message) debug only
	update.message.reply_text(message)