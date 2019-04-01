from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/join.html')
def join():
  return render_template('join.html')


@app.route("/agm2019/")
@app.route("/agm2019/index.html")
def agm2019():
  return render_template('agm2019.html')
