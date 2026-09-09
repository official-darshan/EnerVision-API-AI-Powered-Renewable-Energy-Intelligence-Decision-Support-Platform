def test_weather_rejects_invalid_latitude(client):
    response = client.get("/api/v1/weather?lat=999&lon=72.8777")
    assert response.status_code == 422


def test_weather_rejects_missing_params(client):
    response = client.get("/api/v1/weather")
    assert response.status_code == 422


def test_weather_returns_data_with_mocked_api(client, mocker):
    fake_response_data = {
        "latitude": 19.09,
        "longitude": 72.86,
        "current": {
            "temperature_2m": 29.0,
            "windspeed_10m": 12.0,
            "cloudcover": 40,
            "shortwave_radiation": 500,
            "time": "2026-09-10T12:00",
        },
    }

    mock_response = mocker.Mock()
    mock_response.json.return_value = fake_response_data
    mock_response.raise_for_status.return_value = None

    mocker.patch("app.services.weather_service.httpx.get", return_value=mock_response)

    response = client.get("/api/v1/weather?lat=19.0760&lon=72.8777")

    assert response.status_code == 200
    data = response.json()
    assert data["temperature_celsius"] == 29.0
    assert data["cloud_cover_percent"] == 40
    