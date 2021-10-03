from flask import Flask, render_template
import sys
import os
sys.path.append(os.path.abspath('.'))
from db.database import DB
from google_maps_route import GoogleMapsWrapper

app = Flask(__name__)

myDB = DB()
gmaps_wrapper = GoogleMapsWrapper()
start = "106 Zephyr Bend Place, The Woodlands, TX"
end = "4800 Calhoun Rd, Houston, TX"
THRESHOLD = 0.00045

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/routes/<origin>/<dest>')
def routes(origin, dest):
    raw_routes = gmaps_wrapper.extract_directions(origin, dest)['routes']
    routes = gmaps_wrapper.get_coordinate_path(raw_routes)
    count = 0
    overlap = {}
    for route in routes:
        overlap[f'Route-{count}'] = myDB.QueryAccidents(route, THRESHOLD)
        overlap['num'] = len(overlap[f'Route-{count}'])
    return overlap

if __name__ == '__main__':
    app.run(debug=True)