from flask_frozen import Freezer
from main import app

app.config['FREEZER_DESTINATION_IGNORE'] = ['.git*', 'CNAME']
freezer = Freezer(app)

if __name__ == '__main__':
  freezer.freeze()
