from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from CNNClassifier.utils.common import decodeImage
from CNNClassifier.pipeline.prediction import PredictionPipeline
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

# Initialize the classifier
try:
    clApp = ClientApp()
    logger.info("Model loaded successfully")
except Exception as e:
    logger.error(f"Failed to load model: {e}")
    clApp = None


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')




@app.route("/train", methods=['GET','POST'])
@cross_origin()
def trainRoute():
    # os.system("python main.py")
    os.system("dvc repro")
    return "Training done successfully!"



@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    try:
        if clApp is None:
            return jsonify({"error": "Model not loaded"}), 500
        
        if 'image' not in request.json:
            return jsonify({"error": "No image provided"}), 400
            
        image = request.json['image']
        decodeImage(image, clApp.filename)
        result = clApp.classifier.predict()
        return jsonify(result)
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

