from flask import Flask, request, jsonify
import pickle
import pandas as pd

application = Flask(__name__)

# Load your model and encoders
model = pickle.load(open('model.pkl', 'rb'))
crop_encoder = pickle.load(open('crop_encoder.pkl', 'rb'))
fertilizer_encoder = pickle.load(open('fertilizer_encoder.pkl', 'rb'))

@application.route('/predict', methods=['POST'])
def predict():
    # Get data from Post request
    data = request.get_json()
    
    # Make prediction
    try:
        encoded_crop = crop_encoder.transform([data['crop_type']])[0]
        input_data = pd.DataFrame([[encoded_crop, data['moisture'], data['nitrogen'], data['potassium'], data['phosphorous']]],
                                  columns=["CropType", "Moisture", "Nitrogen", "Potassium", "Phosphorous"])
        
        prediction = model.predict(input_data)[0]
        decoded_prediction = fertilizer_encoder.inverse_transform([prediction])[0]
        
        # Return prediction
        return jsonify({'prediction': decoded_prediction})
    except Exception as e:
        return jsonify({'error': str(e), 'message': 'Error occurred during prediction'}), 400

if __name__ == '__main__':
    application.run(port=5000, debug=True)
