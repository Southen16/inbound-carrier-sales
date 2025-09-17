import os
import json
import requests
import logging
from flask import Blueprint, request, jsonify
from typing import List

bp = Blueprint("carriers", __name__)
FMCSA_BASE_URL = "https://mobile.fmcsa.dot.gov/qc/services/"
fmcsa_api_key = None

# Set up logging
logger = logging.getLogger("carriers")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")
handler.setFormatter(formatter)
if not logger.hasHandlers():
    logger.addHandler(handler)

def init_app(app, api_key):
    global fmcsa_api_key
    fmcsa_api_key = api_key
    app.register_blueprint(bp)
    logger.info("Blueprint registered and FMCSA API key initialized.")
    
def get_loads(origin: str, destination: str) -> List[dict]:
    url = f"{FMCSA_BASE_URL}loads"
    headers = {"web_key": fmcsa_api_key}
    params = {"origin": origin, "destination": destination}
    logger.info(f"Requesting loads from FMCSA API: url={url}, params={params}")
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    logger.info(f"FMCSA API response status: {response.status_code}")
    return response.json().get("loads", [])


def verify_mc_number(mc_number: str) -> bool:
    url = f"{FMCSA_BASE_URL}carriers/{mc_number}/mc-numbers?webKey={fmcsa_api_key}"
    logger.info(f"Verifying MC number: {mc_number} via {url}")
    response = requests.get(url)
    if response.status_code != 200:
        logger.warning(f"FMCSA API returned status {response.status_code} for MC number {mc_number}")
        return False
    data = response.json()
    content = data.get("content", [])
    for item in content:
        if item.get("prefix") == "MC":
            logger.info(f"MC number {mc_number} is valid.")
            return True
    logger.info(f"MC number {mc_number} is NOT valid.")
    return False


@bp.route("/verify_mc_number")
def verify_mc_number_route():
    mc_number = request.args.get("mc_number")
    if not mc_number:
        logger.error("mc_number parameter missing in request.")
        return jsonify({"error": "mc_number is required"}), 400
    is_valid = verify_mc_number(mc_number)
    logger.info(f"MC number verification result: {mc_number} valid={is_valid}")
    return jsonify({"mc_number": mc_number, "valid": is_valid})


@bp.route("/loads")
def get_loads_route():
    json_path = os.path.join(os.getcwd(), "data", "sample_loads.json")
    logger.info(f"Loading sample loads from {json_path}")
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            loads = json.load(f)
        logger.info(f"Loaded {len(loads)} loads from sample_loads.json")
    except Exception as e:
        logger.error(f"Could not read loads: {str(e)}")
        return jsonify({"error": f"Could not read loads: {str(e)}"}), 500
    return jsonify({"loads": loads})
