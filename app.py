from json import *
from flask import Flask, render_template, jsonify, request
from main import Main

main = Main()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def startCounter():
    fs.startPulse()
    return '200'

@app.route('/stop')
def stopCounter():
    fs.stopPulse()
    fs.clearPulse()
    return '200'

@app.route('/pulse')
def getPulse():
    return jsonify(fs.getPulse())

@app.route('/liters')
def getLiters():
    return jsonify(main.getAllTaps())

if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=1122)

