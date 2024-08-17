from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Prediction
from ml_model import predict_price
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']

    if file:
         # simpan filenya untuk sementara
        filename = 'temp.csv'
        file.save(filename)

        # Melakukan ramalan
        prediction = predict_price(filename)

        # Simpan hasil ramalan ke database
        new_prediction = Prediction(result=str(prediction))
        db.session.add(new_prediction)
        db.session.commit()

        # Hapus filenya untuk sementara waktu
        os.remove(filename)

        return jsonify({'prediction': prediction})
    return jsonify({'error': 'KAGAK ADA FILENYA'}), 400

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)