from flask import Flask, request, render_template, url_for
import pickle
import numpy as np
import pandas as pd
from sklearn.linear_model import SGDRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

app = Flask(__name__)

df = pd.read_csv("clean_data.csv")

y = df.iloc[:, 7].values
X = df.iloc[:, [6, 16, 17]].values


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

pipeline = Pipeline([
    ('std_scalar', StandardScaler())
])

X_train = pipeline.fit_transform(X_train)
X_test = pipeline.transform(X_test)

sgd_reg = SGDRegressor(n_iter_no_change=250, penalty=None, eta0=0.0001, max_iter=100000)
sgd_reg.fit(X_train, y_train)

filename = 'model.pkl'
pickle.dump(sgd_reg, open(filename, 'wb'))
model = pickle.load(open(filename, 'rb'))

@app.route('/')
def index():
    return render_template('index.html', Rainfall=0)

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Prediksi cuaca berdasarkan input kelembapan, latitude, longitude
    '''
    AVG_humidity, latitude, longitude = [x for x in request.form.values()]

    AVG_humidity  = float(AVG_humidity)
    latitude = float(latitude)
    longitude = float(longitude)

    #data = np.array(input, dtype=float)
    
    # prediction = model.predict([data])
    prediction = sgd_reg.predict([[AVG_humidity, latitude, longitude]])
    output = round(prediction[0], 2)/4.5


    return render_template('index.html', Rainfall=output, AVG_humidity=AVG_humidity, latitude=latitude, longitude=longitude)


if __name__ == '__main__':
    app.run(debug=True)