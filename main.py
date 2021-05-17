from flask import Flask
from flask import jsonify
from models import db
from models import Day
from config import config
from datetime import datetime
import requests
import pytest
import click


def create_app():
    app = Flask(__name__)
    app.config.from_object(config['development'])
    with app.app_context():
        db.init_app(app)
        db.create_all()

    @app.route('/days', methods=['GET'])
    def get_days():
        days_query = Day.query
        days = [ day.json() for day in days_query.all() ] 
        return jsonify({'days': days })

    @app.route('/days/<location>', methods=['GET'])
    def get_days_by_location(location):
        days_query = Day.query.filter_by(location=location)
        days = [ day.json() for day in days_query.all() ] 
        return jsonify({'days': days })

    @app.cli.command()
    def test():
        """Run tests"""
        pytest.main(['tests.py'])

    @app.cli.command()
    @click.argument("location")
    def getdata(location):
        """Get data from TuTiempo API"""
        print('Importing days...')

        response = requests.get(config['tutiempo_url'].format(location))
        data = response.json()
        for i in range(7):
            day = data['day' + str(i+1)]
            day['location'] = location
            add_day(data['day' + str(i+1)])

        print('Done!')

    def add_day(day):
        date = datetime.strptime(day['date'], '%Y-%m-%d').date()
        location = day['location']

        d = Day.query.filter_by(date=date, location=location).first()
        if d is None:
            d = Day()

        d.load_from_json(day)
        d.save()

    return app

app = create_app()
    
if __name__ == '__main__':
    app.run(debug=True)
