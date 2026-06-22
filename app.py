import requests
from flask import Flask, jsonify
from flask_cors import CORS
import os
import json  # 워터마크 설정을 위해 추가된 부품입니다.

app = Flask(__name__)
CORS(app)

@app.route('/get-vdo-otp/<video_id>')
def get_otp(video_id):
    url = f"https://dev.vdocipher.com/api/videos/{video_id}/otp"
    headers = {
        "Authorization": "Apisecret HHYuT5w17YfmOZGm4gFwEAl1GfpSyrMs3NdjyCShlnOIChEhnU4xFrkMwby95Ko5",
        "Content-Type": "application/json"
    }

    # 💡 워터마크 문구와 디자인을 설정하는 부분입니다.
    watermark_config = [
        {
            "type": "rtext",
            "text": "마음침법 VOD 불법유출 모니터링 중\n접속 IP: {ip}\n시간: {date}",
            "alpha": 0.5,        # 투명도 (1.0으로 갈수록 진해짐, 0.5는 반투명)
            "color": "0xFFFFFF", # 글자색 (현재 흰색)
            "size": 15,          # 글자 크기
            "interval": 5000,    # 5초마다 화면의 다른 위치로 휙휙 이동
            "skip": 2000         # 이동하기 전 2초 동안은 화면에서 사라짐 (강의 가림 방지)
        }
    ]

    payload = {
        "ttl": 300,
        "annotate": json.dumps(watermark_config)
    }

    response = requests.post(url, headers=headers, json=payload)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
