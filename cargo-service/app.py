from flask import Flask, jsonify

app = Flask(__name__)

cargo_list = [
    {"container": "CNT001", "cargo": "Electronics", "destination": "Mumbai Port", "status": "In Transit"},
    {"container": "CNT002", "cargo": "Textiles", "destination": "Chennai Port", "status": "Delivered"},
    {"container": "CNT003", "cargo": "Machinery", "destination": "Kolkata Port", "status": "Loading"},
]

@app.route('/')
def home():
    return jsonify({"service": "Cargo Tracking Service", "status": "running"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/api/cargo')
def get_cargo():
    return jsonify(cargo_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
