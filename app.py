from flask import Flask, render_template, Response, request
import os
import pprint

app = Flask(__name__)

@app.route('/fulfill', methods=['POST'])
def home():
	print request.json
	print request.query_string
	return Response(
		'{"fulfillmentText":"this response came from fulfillment"}',
		mimetype='application/json'
	) 
	# return render_template('home.html')

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port, threaded=True, debug=True)