from flask import Flask, request, render_template
import random

app = Flask(__name__, static_url_path='/static')

# In-memory data (replace with a database for a real application)
rides = {}
next_ride_id = 1

def calculate_fare(distance):
    """Simple fare calculation based on distance."""
    return 5 + 1.5 * distance  # Base fare + per-mile charge

def find_driver():
    """Placeholder for driver matching logic."""
    # In reality, you would use location data and driver availability
    drivers = ["Driver1", "Driver2", "Driver3"]
    return random.choice(drivers) if drivers else None

@app.route('/')
def index():
    return render_template('request_ride.html')

@app.route('/request_ride', methods=['POST'])
def request_ride():
    global next_ride_id
    origin = request.form['origin']
    destination = request.form['destination']

    # In a real app, you would calculate the distance using a map API
    distance = random.uniform(1, 10)  # Simulate distance calculation

    driver = find_driver()
    if not driver:
        return "No drivers available at the moment."

    fare = calculate_fare(distance)

    ride_id = next_ride_id
    next_ride_id += 1

    rides[ride_id] = {
        'origin': origin,
        'destination': destination,
        'driver': driver,
        'fare': fare,
        'distance': distance,
        'status': 'requested'
    }

    return render_template('ride_confirmation.html', ride_id=ride_id, origin=origin, destination=destination, fare=fare, driver=driver)

@app.route('/track_ride/<int:ride_id>')
def track_ride(ride_id):
    ride = rides.get(ride_id)
    if not ride:
        return "Ride not found."

    # Simulate ride progress
    ride['status'] = 'in progress'
    return render_template('track_ride.html', ride=ride)

if __name__ == '__main__':
    app.run(debug=True)
