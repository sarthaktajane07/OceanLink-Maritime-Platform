from flask import Flask, jsonify

app = Flask(__name__)

weather_data = [
    {"location": "Arabian Sea", "temperature": "29C", "wind_speed": "15 km/h", "condition": "Clear"},
    {"location": "Bay of Bengal", "temperature": "31C", "wind_speed": "25 km/h", "condition": "Cloudy"},
    {"location": "Mumbai Port", "temperature": "30C", "wind_speed": "10 km/h", "condition": "Clear"},
]

@app.route('/')
def home():
    return jsonify({"service": "Weather Service", "status": "running"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/api/weather')
def get_weather():
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
