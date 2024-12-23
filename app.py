from flask import Flask, request, jsonify
import sys
import os
import uuid
import logging
import subprocess
import json

# Add the scrappy directory to sys.path
SCRAPPY_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../scrappy'))
sys.path.append(SCRAPPY_PATH)

from scrappy.main import main as scrappy_main  # Import the main function from scrappy

app = Flask(__name__)

# Temporary storage for confirmation states
confirmation_states = {}

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def set_scrappy_env(owner_names):
    """Set environment variables for Scrappy."""
    os.environ["SCRAPPY_OWNERS"] = ";".join(owner_names)
    os.environ["SCRAPPY_EXTERNAL_CONFIRMATION"] = "true"

@app.route('/')
def home():
    """Basic health check endpoint."""
    return jsonify({"message": "Welcome to ScrapFlask API!"})

@app.route('/scrape', methods=['POST'])
def scrape():
    """Endpoint to trigger scrappy with provided owner names."""
    data = request.get_json()
    logger.info(f"Received payload: {data}")

    owner_names = data.get("owners")
    if not owner_names:
        logger.warning("No owners provided in the request.")
        return jsonify({"error": "No owners provided"}), 400

    try:
        logger.info(f"Triggering Scrappy for owners: {owner_names}")
        set_scrappy_env(owner_names)

        # Run Scrappy and capture its JSON output
        result = subprocess.run(
            [sys.executable, os.path.join(SCRAPPY_PATH, "main.py")],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode != 0:
            logger.error(f"Scrappy encountered an error: {result.stderr}")
            return jsonify({"error": "Scrappy failed", "details": result.stderr}), 500

        # Parse JSON output from Scrappy
        try:
            scrappy_output = json.loads(result.stdout)
        except json.JSONDecodeError as e:
            logger.error(f"Failed to decode JSON output from Scrappy: {e}")
            return jsonify({"error": "Invalid JSON output from Scrappy"}), 500

        logger.info(f"Scraping successfully completed for owners: {owner_names}")
        return jsonify({"message": "Scraping completed!", "data": scrappy_output})

    except Exception as e:
        logger.error(f"Error in /scrape endpoint: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/confirm', methods=['POST'])
def confirm():
    """Endpoint to handle user confirmation for fuzzy matches."""
    data = request.get_json()
    owner = data.get("owner")
    match = data.get("match")
    confirmation = data.get("confirmation")

    if not owner or not match or confirmation not in ["yes", "no"]:
        logger.warning("Invalid confirmation payload.")
        return jsonify({"error": "Invalid confirmation payload"}), 400

    logger.info(f"Received confirmation: {confirmation} for owner '{owner}' and match '{match}'")
    os.environ["SCRAPPY_CONFIRMATION"] = confirmation
    return jsonify({"message": "Confirmation received. Resuming Scrappy."})

if __name__ == '__main__':
    app.run(debug=True)
