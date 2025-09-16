import os
import json
import requests
from flask import Blueprint, request, jsonify
import os
import json
from typing import List

bp = Blueprint("carriers", __name__)
FMCSA_BASE_URL = "https://mobile.fmcsa.dot.gov/qc/services/"
fmcsa_api_key = None

def init_app(app, api_key):
    global fmcsa_api_key
    fmcsa_api_key = api_key
    app.register_blueprint(bp)
    
def get_loads(origin: str, destination: str) -> List[dict]:
    url = f"{FMCSA_BASE_URL}loads"
    headers = {"web_key": fmcsa_api_key}
    params = {"origin": origin, "destination": destination}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json().get("loads", [])


def verify_mc_number(mc_number: str) -> bool:
    url = f"{FMCSA_BASE_URL}carriers/{mc_number}/mc-numbers?webKey={fmcsa_api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        return False
    data = response.json()
    content = data.get("content", [])
    for item in content:
        if item.get("prefix") == "MC":
            return True
    return False


@bp.route("/verify_mc_number")
def verify_mc_number_route():
    mc_number = request.args.get("mc_number")
    if not mc_number:
        return jsonify({"error": "mc_number is required"}), 400
    is_valid = verify_mc_number(mc_number)
    return jsonify({"mc_number": mc_number, "valid": is_valid})


@bp.route("/loads")
def get_loads_route():
    # Use local sample_loads.json for demo
    json_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "sample_loads.json")
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            loads = json.load(f)
    except Exception as e:
        return jsonify({"error": f"Could not read loads: {str(e)}"}), 500
    return jsonify({"loads": loads})
