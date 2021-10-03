from flask import Flask, render_template
import sys
import os
sys.path.append(os.path.abspath('.'))
from db.database import DB

app = Flask(__name__)

myDB = DB()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)