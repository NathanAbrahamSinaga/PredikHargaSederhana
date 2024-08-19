from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, PredictionData
from ml_model import predict_price
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    if file:
        # Simpan file sementara
        file_path = 'temp.csv'
        file.save(file_path)
        
        # Lakukan prediksi
        prediction = predict_price(file_path)
        
        # Simpan hasil prediksi ke database
        new_prediction = PredictionData(result=prediction)
        db.session.add(new_prediction)
        db.session.commit()
        
        # Hapus file sementara
        os.remove(file_path)
        
        return jsonify({'prediction': prediction})
    return jsonify({'error': 'No file uploaded'}), 400

if __name__ == '__main__':
    app.run(debug=True)