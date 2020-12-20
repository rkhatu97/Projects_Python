import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
model = pickle.load(open('sentiment_classifier.pkl', 'rb'))
vector = pickle.load(open('vectorizer.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    #label = {0: ‘negative’, 1: ‘positive’}
    int_features = [x for x in request.form.values()]
    int_features = vector.transform(int_features)
    proba = model.predict(int_features)[0]

    return render_template('index.html', prediction_text='Review: {}'.format(proba))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    data = vector.transform(data)
    proba = model.predict_proba(data[0])

    output = proba
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)