from flask import Flask, request
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
	if 'url' in request.args:
		r = requests.get(request.args['url'])
		return  r.content
	else:
		return '''
		<form method = 'get'>
		<input type="text" name="url">
		<input type="submit" value="Отправить">
		</form>
		'''
if __name__ == '__main__':
	app.run()