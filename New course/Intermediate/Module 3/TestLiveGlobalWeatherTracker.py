import pytest
from LiveGlobalWeatherTracker import City, Tracker

@pytest.fixture
def tracker():
    return Tracker

@pytest.mark.api_mock
def test_weather_mocked(tracker, mocker):
    mock_reponse = mocker.Mock()
    mock_reponse.status_code = 200
    mock_reponse.json.return_value = {
        "current":{
            "temp_c": 22.5,
            "condition": {"text": "Sunny"},
            "humidity": 50
        }
    }
    mocker.patch("LiveGlobalWeatherTracker.requests.get", return_value=mock_response)

    city = City("Mockville", "Nowhere")
    tracker.add_cities(city)

    weather = tracker.weather_records[city]
    assert -5 < weather.temperature <60, "Temperature is out of range"
    assert isinstance(weather.condition, str) and weather.condition.strip()!= ""
    assert 0 <= weather.humidity <=100

@pytest.mark.api_live
@pytest.mark.parametrize("city_name, country", [
    ("London", "UK"),
    ("Tokyo", "Japan"),
])

def test_api_call(tracker, city_name, country):
    city = City(city_name, country)
    tracker.add_cities(city)

    assert len(tracker) == 1
    weather = tracker.weather_records[city]

    assert -5 < weather.temperature <60, "Temperature is out of range"
    assert isinstance(weather.condition, str) and weather.condition.strip()!= ""
    assert 0 <= weather.humidity <=100