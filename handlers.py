from random import randint
import telegram

def dado(num):
	return randint(1,num)
	
def d4(bot,update):
	update.message.reply_text(str(dado(4)))

def d6(bot,update):
	update.message.reply_text(str(dado(6)))

def d8(bot,update):
	update.message.reply_text(str(dado(8)))

def d10(bot,update):
	update.message.reply_text(str(dado(10)))

def d12(bot,update):
	update.message.reply_text(str(dado(12)))

def d20(bot,update):
	update.message.reply_text(str(dado(20)))

def d100(bot,update):
	update.message.reply_text(str(dado(100)))

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
		tot+=MP
	if MM>0:
		toreturn+=" - " + str(MM) + " = " + str(tot-MM)
	return toreturn
	

def tiradadi(bot,update,args):
	message = ''
	if not args:
		message = "lancia n dadi di tipo x, puoi aggiungere o togliere y: /tira ndx+y, puoi scrivere espressioni differenti, separate da uno spazio"
	else:
		primo = True
		for arg in args:
			toreturn = ''
			if "#" in arg:
				toreturn+=" "+arg
			else:
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
	
def callKeyboard(bot,update,args):
	#message = ''
	custom_keyboard = [['top-left', 'top-right'],['bottom-left', 'bottom-right']]
	reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
	update.message.reply(chat_id=chat_id, 
                  text="Custom Keyboard Test", 
                  reply_markup=reply_markup)
	#update.message.reply_text(message)