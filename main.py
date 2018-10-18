from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
  return "Welcome to GWU Sweden, a local chapter of Game Workers Unite. Nothing here yet but do check back soon."
