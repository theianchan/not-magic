from flask import Flask, render_template

import pandas as pd

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/models')
def models():
  return render_template('models.html')

@app.route('/model')
def model():
  url = "sample-datasets/advertising.csv"
  ad_data = pd.read_csv(url)

  data = {}
  data['head'] = ad_data[1:4].to_html(classes='table table-striped table-bordered')
  data['corr'] = ad_data.corr().to_html(classes='table table-striped table-bordered')
  return render_template('model.html', data=data)

if __name__ == '__main__':
  app.run(debug=DEBUG, host=HOST, port=PORT)
