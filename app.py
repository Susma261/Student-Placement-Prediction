from flask import *
import numpy as np
import pandas as pd
import pickle
import jsonify

app = Flask(__name__)
model = pickle.load(open('log_reg.pkl','rb'))
@app.route('/')
def Home():
    return render_template('index.html')


@app.route("/predict",methods=['POST'])
def predict():
    if request.method=='POST':
        gender = int(request.form['gender'])
        ssc_per = float(request.form['ssc_per'])        
        hsc_per = float(request.form['hsc_per'])
        degree_stream = int(request.form['degree_stream'])  
        degree_per = float(request.form['degree_per'])        
        wrk_exp = int(request.form['wrk_exp'])
        spec = int(request.form['spec'])
        mba = float(request.form['mba'])

        prediction = model.predict([[gender,ssc_per,hsc_per,degree_stream,degree_per,wrk_exp,spec,mba]])
        pred = round(prediction[0],2)
        out = "Error"
        if pred ==1: out = "You got Placed!!"
        else: out = "You are Not Placed!!"
        return render_template('index.html',results=out)
    else:
        return render_template('index.html')
if __name__ == "__main__":
    	app.run(debug = True)


