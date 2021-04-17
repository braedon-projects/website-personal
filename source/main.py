from flask import Flask, render_template, request, redirect, url_for, send_file
from driver import bmi, retirement
app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        if 'resume' in request.form:
            return redirect(url_for('braedonresume'))
        if 'portfolio' in request.form:
            return redirect(url_for('retirementpage'))
    return render_template('index.html')

@app.route('/braedonresume', methods=['POST', 'GET'])
def braedonresume():
    if request.method == 'POST':
        return render_template('braedonresume.html')
    return render_template('braedonresume.html')

@app.route('/retirementpage', methods=['POST', 'GET'])
def retirementpage():
    if request.method == 'POST':
        return render_template('retirement.html')
    return render_template('retirement.html')

if __name__ == '__main__':
    app.run(debug=True, port=4321)

    #This comment is so I can make a commit/push for the report lol