from flask import Flask
from flask import jsonify
from models import db
from models import Day
from config import config
from datetime import datetime
import requests
import sys


app = Flask(__name__)
app.config.from_object(config['development'])
with app.app_context():
    db.init_app(app)
    db.create_all()

@app.route('/days', methods=['GET'])
def get_days():
    days = [ day.json() for day in Day.query.all() ] 
    return jsonify({'days': days })

@app.route('/days/<date>', methods=['GET'])
def get_day(date):
    date = datetime.strptime(date, '%Y-%m-%d').date()
    day = Day.query.filter_by(date=date).first()
    if day is None:
        return jsonify({'message': 'Day does not exists'}), 404

    return jsonify({'day': day.json() })

@app.cli.command()
def getdata():
    """Get data from TuTiempo API"""
    print('Importing days...')
    get_data()
    print('Done!')

def get_data():
    response = requests.get(config['tutiempo_url'])
    data = response.json()
    for i in range(7):
        add_day(data['day' + str(i+1)])

def add_day(day):
    date = datetime.strptime(day['date'], '%Y-%m-%d').date()

    d = Day.query.filter_by(date=date).first()
    if d is None:
        d = Day()
        d.date = date

    d.temperature_max = day['temperature_max']
    d.temperature_min = day['temperature_min']
    d.icon = day['icon']
    d.text = day['text']
    d.humidity = day['humidity']
    d.wind = day['wind']
    d.wind_direction = day['wind_direction']
    d.icon_wind = day['icon_wind']
    d.sunrise = day['sunrise']
    d.sunset = day['sunset']
    d.moonrise = day['moonrise']
    d.moonset = day['moonset']
    d.moon_phases_icon = day['moon_phases_icon']

    d.save()
    
if __name__ == '__main__':
    app.run(debug=True)