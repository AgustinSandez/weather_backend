from datetime import datetime
from models import Day
from main import create_app
import pytest


@pytest.fixture
def test_client():
    app = create_app()
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as test_client:
            yield test_client

def test_day_load_from_json():
    json = {
                "date":"2021-05-20",
                "humidity":47,
                "icon":"2",
                "icon_wind":"SO",
                "moon_phases_icon":"9",
                "moonrise":"14:24",
                "moonset":"03:43",
                "sunrise":"6:56",
                "sunset":"21:27",
                "temperature_max":29,
                "temperature_min":14,
                "text":"Nubes dispersas",
                "wind":11,
                "wind_direction":"Suroeste"
            }
    day = Day()
    day.load_from_json(json)

    assert day.date == datetime(2021, 5, 20).date()
    assert day.humidity == 47
    assert day.icon == "2"
    assert day.icon_wind == "SO"
    assert day.moon_phases_icon == "9"
    assert day.moonrise == "14:24"
    assert day.moonset == "03:43"
    assert day.sunrise == "6:56"
    assert day.sunset == "21:27"
    assert day.temperature_max == 29
    assert day.temperature_min == 14
    assert day.text == "Nubes dispersas"
    assert day.wind == 11
    assert day.wind_direction == "Suroeste"
    
def test_root_404(test_client):
    response = test_client.get('/')
    assert response.status_code == 404

def test_get_days_200(test_client):
    response = test_client.get('/days')
    assert response.status_code == 200

def test_get_fake_day(test_client):
    response = test_client.get('/days/1900-01-01')
    assert response.status_code == 404

def test_get_days(test_client):
    response = test_client.get('/days')
    assert response.status_code == 200
    assert b'days' in response.data