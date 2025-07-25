# app.py

from flask import Flask, render_template, request
from src.mlProject.pipeline.prediction import predict

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_data = request.form.to_dict()
        result = predict(input_data)
        return render_template('index.html', result=result, form_data=input_data)
    return render_template('index.html', result=None, form_data={})

if __name__ == "__main__":
    app.run(debug=True)
