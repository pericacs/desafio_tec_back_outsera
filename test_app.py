
import os
import sys

import pytest

from app import Movie, app, db

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            movie1 = Movie(year=1980, title="Test Movie 1", producers="Producer A", winner=True)
            movie2 = Movie(year=1985, title="Test Movie 2", producers="Producer A", winner=True)
            movie3 = Movie(year=1981, title="Test Movie 3", producers="Producer B", winner=True)
            movie4 = Movie(year=1982, title="Test Movie 4", producers="Producer B", winner=True)
            db.session.add_all([movie1, movie2, movie3, movie4])
            db.session.commit()
        yield client

def test_intervals(client):
    response = client.get('/producers/intervals')
    assert response.status_code == 200
    data = response.get_json()
    assert "min" in data
    assert "max" in data
    assert data["min"]["producer"] == "Producer B"
    assert data["min"]["interval"] == 1
    assert data["max"]["producer"] == "Producer A"
    assert data["max"]["interval"] == 5
