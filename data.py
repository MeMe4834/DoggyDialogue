from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/disease_info.html')
def disease_info():
    return render_template('disease_info.html')

@app.route('/')
def index():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)