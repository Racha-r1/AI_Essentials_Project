from flask import Flask, request , json
import joblib
import os
from sklearn.preprocessing import StandardScaler
import numpy as np

app = Flask(__name__)

def checklabel(label):
    mapping = {
        0: "Bad",
        1: "Mediocre",
        2: "Good"
    }
    return mapping[label]

@app.route('/knn', methods=['POST'])
def predict_knn():
    # first load the model
    dirname = os.getcwd()
    filename_knn = os.path.join(dirname, 'models/knn')
    knn = joblib.load(filename_knn)
    # read the request data from the post request
    response = request.get_json()
    data = json.loads(response["data"])
    # convert the data into a numpy array
    arr = np.array(data)
    # scale the data
    scaler = StandardScaler()
    arr = scaler.fit_transform(arr)
    # predict the response
    predictions = knn.predict(arr)
    labels = map(checklabel, predictions.tolist())
    labels = list(labels)
    return json.dumps(labels)

@app.route('/random-forest', methods=['POST'])
def predict_random_forest():
     # first load the model
    dirname = os.getcwd()
    filename_randomforest = os.path.join(dirname, 'models/randomforest')
    randomforest = joblib.load(filename_randomforest)
    # read the request data from the post request
    response = request.get_json()
    data = json.loads(response["data"])
    # convert the data into a numpy array
    arr = np.array(data)
    # scale the data
    scaler = StandardScaler()
    arr = scaler.fit_transform(arr)
    # predict the response
    predictions = randomforest.predict(arr)
    labels = map(checklabel, predictions.tolist())
    labels = list(labels)
    return json.dumps(labels)

if __name__ == '__main__':
    app.run(host='0.0.0.0')