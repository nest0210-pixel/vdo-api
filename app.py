import requests
from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/get-vdo-otp/<video_id>')
def get_otp(video_id):
    url = f"https://api.vdocipher.com/v2/customer/api/videos/{video_id}/otp"
    headers = {
        "Authorization": "Apisecret HHYuT5w17YfmOZGm4gFwEAl1GfpSyrMs3NdjyCShlnOIChEhnU4xFrkMwby95Ko5",
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json={"ttl": 300})
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
