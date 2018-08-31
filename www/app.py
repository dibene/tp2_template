# Imports
from flask import Flask
from flask import render_template
from aux_pro import Process
from database import Database
from flask import jsonify
from pprint import pprint

app = Flask(__name__)
db = Database()
pro = Process()
import sys
import json

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stop')
def stopAction():
    pro.stop_process()
    return render_template('index.html')

@app.route('/start')
def startAction():
    pro.start_process()
    return render_template('index.html')

@app.route('/lastten', methods = ["GET"])
def lastTenAction():
    samples = db.getSamples()
    print('[%s]' % ', '.join(map(str, samples)))
    sys.stdout.flush()
    jsonSamples=[]
    for s in samples:
        jsonSamples.append(s.serialize())
    print('[%s]' % ', '.join(map(str, jsonSamples)))

    sys.stdout.flush()
    return jsonify(jsonSamples)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)

