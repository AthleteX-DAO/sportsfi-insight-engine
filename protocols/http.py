# protocols/http_protocol.py
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/fetch', methods=['GET'])
def fetch_data():
    try:
        # Fetch live market data from CoinGecko
        response = requests.get("")
        response.raise_for_status()  # Raise an HTTPError for bad responses
        sportsfi_info = response.json()
        return jsonify({"data": sportsfi_info})
    except requests.exceptions.RequestException as e:
        # Log the error details for debugging
        print(f"Error fetching market data: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/process', methods=['POST'])
def process_data():
    data = request.json
    processed_data = {k: round(v, 2) for k, v in data.get("data", {}).items()}
    return jsonify({"processed_data": processed_data})

@app.route('/log', methods=['POST'])
def log_data():
    data = request.json
    print(f"Logged Data: {data}")
    return jsonify({"status": "success", "logged_data": data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
