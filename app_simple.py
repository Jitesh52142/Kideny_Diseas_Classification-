from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/train", methods=['GET','POST'])
@cross_origin()
def trainRoute():
    return "Training endpoint - not available in simple mode"

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    try:
        if 'image' not in request.json:
            return jsonify({"error": "No image provided"}), 400
            
        # Mock prediction for testing
        result = [{"image": "Normal"}]
        return jsonify(result)
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
