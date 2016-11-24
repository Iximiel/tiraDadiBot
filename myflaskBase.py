from flask import Flask

app = Flask(__name__)

@app.route('/')
def explanation():
	return "<par>I'm creating this to make a Telegram bot for my friends<br>and I'm actually enjoing it(more or <b>less</b>)!!</par>"

	
if __name__ == '__main__':
	app.run()