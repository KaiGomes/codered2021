from flask import Flask, render_template
import sys
import os
sys.path.append(os.path.abspath('.'))
from db.database import DB
from google_maps_route import GoogleMapsWrapper
from scoreCalc import Route

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
    overlap = {}
    raw_routes = gmaps_wrapper.extract_directions(origin, dest)
    overlap['num_routes'] = len(raw_routes)
    distances = [route['legs'][0]['distance']['value'] for route in raw_routes]
    routes = gmaps_wrapper.get_coordinate_path(raw_routes)
    count = 0
    
    for distance, route in zip(distances, routes):
        overlap[f'Route-{count}'] = myDB.QueryAccidents(route, THRESHOLD)
        num = len(overlap[f'Route-{count}'])
        total_sev = sum([sev['severity'] for sev in overlap[f'Route-{count}']])
        # new_route = Route(f'Route-{count}', total_sev, num,  distance)
        danger_score = total_sev / float(distance)
        # overlap[f'Route-{count}'] = danger_score
        overlap[f'Route-{count}'] = danger_score
    return overlap

if __name__ == '__main__':
    app.run(debug=True)