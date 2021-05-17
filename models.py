from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Day(db.Model):
    __tablename__ = 'days'

    date = db.Column(db.Date, primary_key=True)
    location = db.Column(db.String(10), primary_key=True)
    temperature_max = db.Column(db.Integer)
    temperature_min = db.Column(db.Integer)
    icon = db.Column(db.String(10))
    text = db.Column(db.String(50))
    humidity = db.Column(db.Integer)
    wind = db.Column(db.Integer)
    wind_direction = db.Column(db.String(50))
    icon_wind = db.Column(db.String(10))
    sunrise = db.Column(db.String(20))
    sunset = db.Column(db.String(20))
    moonrise = db.Column(db.String(20))
    moonset = db.Column(db.String(20))
    moon_phases_icon = db.Column(db.String(10))

    def save(self):
        db.session.add(self)
        db.session.commit()

        return self

    def load_from_json(self, day):
        self.date = datetime.strptime(day['date'], '%Y-%m-%d').date()
        self.location = day['location']
        self.temperature_max = day['temperature_max']
        self.temperature_min = day['temperature_min']
        self.icon = day['icon']
        self.text = day['text']
        self.humidity = day['humidity']
        self.wind = day['wind']
        self.wind_direction = day['wind_direction']
        self.icon_wind = day['icon_wind']
        self.sunrise = day['sunrise']
        self.sunset = day['sunset']
        self.moonrise = day['moonrise']
        self.moonset = day['moonset']
        self.moon_phases_icon = day['moon_phases_icon']

    def json(self):
            return {
                "date": self.date,
                "location": self.location,
                "temperature_max": self.temperature_max,
                "temperature_min": self.temperature_min,
                "icon": self.icon,
                "text": self.text,
                "humidity": self.humidity,
                "wind": self.wind,
                "wind_direction": self.wind_direction,
                "icon_wind": self.icon_wind,
                "sunrise": self.sunrise,
                "sunset": self.sunset,
                "moonrise": self.moonrise,
                "moonset": self.moonset,
                "moon_phases_icon": self.moon_phases_icon
            }