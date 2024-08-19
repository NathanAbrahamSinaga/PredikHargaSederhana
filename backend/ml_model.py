import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

def predict_price(file_path):
    # Baca file CSV
    df = pd.read_csv(file_path)
    
    # Asumsikan kolom terakhir adalah target (harga)
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    
    # Preprocessing
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    
    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Prediksi
    prediction = model.predict(X_test)
    
    # Mengembalikan rata-rata prediksi
    return float(prediction.mean())