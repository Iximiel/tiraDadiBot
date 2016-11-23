from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
	return "<par>I'm creating this to make a Telegram bot for my friends<br>and I'm actually enjoing it!!\n</par>"

if __name__ == '__main__':
	app.run()
	