from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"service": "Analytics Service", "status": "running"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/api/analytics')
def get_analytics():
    return jsonify({
        "total_ships": 3,
        "active_cargo": 2,
        "delayed_shipments": 1,
        "fuel_consumption": "1250 tons",
        "ship_traffic_trend": [12, 15, 18, 14, 20, 22, 19],
        "cargo_status_distribution": {
            "In Transit": 1,
            "Delivered": 1,
            "Loading": 1
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
