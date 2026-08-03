"""
API REST para la clasificación automática de facturas P2P.
"""
from flask import Blueprint, request, jsonify
import joblib
import os

api = Blueprint('api', __name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'model', 'model.pkl')

try:
    model = joblib.load(MODEL_PATH)
    MODEL_LOADED = True
except Exception:
    model = None
    MODEL_LOADED = False

@api.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if data is None:
            return jsonify({'error': 'Request body is empty.'}), 400

        text = data.get('text', '').strip()
        if text == '':
            return jsonify({'error': 'Invoice description is required.'}), 400

        if model is None:
            return jsonify({'error': 'Model is not available.'}), 500

        prediction = model.predict([text])[0]
        return jsonify({'prediction': prediction})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route('/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'UP' if MODEL_LOADED else 'DEGRADED',
        'application': 'P2P AI Classification',
        'model_loaded': MODEL_LOADED
    })

@api.route('/version', methods=['GET'])
def version():
    return jsonify({
        'version': '1.0.0',
        'author': 'Jaqueline Lopez Chaidez',
        'framework': 'Flask',
        'machine_learning': 'Scikit-Learn'
    })
