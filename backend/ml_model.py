import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

def predict_price(filename):
    # Baca data
    data = pd.read_csv(filename)

    # preprocessing
    x = data.drop('price', axis=1)
    y = data['price']

    # split data
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # Scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transfrom(X_test)

    # Train model
    model = LinearRegression()
    model.fit(X_train_scaled, y_train)

    # Predisi
    prediction = model.predict(X_test_scaled)

    return prediction.tolist()

