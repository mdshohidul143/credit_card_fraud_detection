import uvicorn
from fastapi import FastAPI
from base import creditCard_fraud
import joblib
app = FastAPI()
jblib = "credit_card_fraud.joblib"
classifier=joblib.load(jblib)

@app.get('/')
def index():
    return {'Deployment': 'Credit Card Fraud Detection'}

@app.post('/predict')
def predict(df:creditCard_fraud):
    data = df.dict()

    Time =data["Time"] 
    V1 = data["V1"] 
    V2  = data["V2"] 
    V3 = data["V3"]
    V4  = data["V4"]
    V5  = data["V5"]
    V6  = data["V6"]
    V7  = data["V7"]
    V8  = data["V8"]
    V9  = data["V9"]
    V10 = data["V10"]
    V11 = data["V11"]
    V12 = data["V12"]
    V13 = data["V13"]
    V14 = data["V14"]
    V15 = data["V15"]
    V16 = data["V16"]
    V17 = data["V17"]
    V18 = data["V18"]
    V19 = data["V19"]
    V20 = data["V20"]
    V21 = data["V21"]
    V22 = data["V22"]
    V23 = data["V23"]
    V24 = data["V24"]
    V25 = data["V25"]
    V26 = data["V26"]
    V27 = data["V27"]
    V28 = data["V28"]
    Amount = data["Amount"]

    prediction = classifier.predict([[Time,V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,Amount]])
    if(prediction[0] == 0):
        prediction="Non Fraud"
    else:
        prediction="Fraud"
    return {
        'prediction': prediction
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5000)
