from flask import Flask, jsonify

app = Flask(__name__)

vessels = [
    {"id": "V001", "name": "Ocean Star", "location": "Arabian Sea", "status": "Sailing"},
    {"id": "V002", "name": "Pacific Dawn", "location": "Mumbai Port", "status": "Docked"},
    {"id": "V003", "name": "Atlantic Wave", "location": "Bay of Bengal", "status": "Delayed"},
]

@app.route('/')
def home():
    return jsonify({"service": "Vessel Tracking Service", "status": "running"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/api/vessels')
def get_vessels():
    return jsonify(vessels)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
