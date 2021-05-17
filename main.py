from flask import Flask
from flask import jsonify
from models import db
from models import Day
from config import config
from datetime import datetime
import requests


def create_app():
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

        response = requests.get(config['tutiempo_url'])
        data = response.json()
        for i in range(7):
            add_day(data['day' + str(i+1)])

        print('Done!')

    def add_day(day):
        date = datetime.strptime(day['date'], '%Y-%m-%d').date()

        d = Day.query.filter_by(date=date).first()
        if d is None:
            d = Day()

        d.load_from_json(day)
        d.save()

    return app

app = create_app()
    
if __name__ == '__main__':
    app.run(debug=True)
