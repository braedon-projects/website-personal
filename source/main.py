from flask import Flask, render_template, request, redirect, url_for
from driver import bmi, retirement
app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        if 'bmi' in request.form:
            return redirect(url_for('bmipage'))
        if 'retirement' in request.form:
            return redirect(url_for('retirementpage'))
    return render_template('index.html')

@app.route('/bmipage', methods=['POST', 'GET'])
def bmipage():
    if request.method == 'POST':
        if request.form['submit'] == 'submit':
            height = float(request.form['height'])
            weight = float(request.form['weight'])
            cat, out, wflag, hflag = bmi(weight, height)
            return render_template('bmi.html', category = cat, message = out)
    return render_template('bmi.html')

@app.route('/retirementpage', methods=['POST', 'GET'])
def retirementpage():
    if request.method == 'POST':
        if request.form['submit'] == 'submit':
            age = float(request.form['age'])
            sal = float(request.form['salary'])
            pcs = float(request.form['percentsaved'])
            sg = float(request.form['savingsgoal'])
            message, flag, pflag, sflag, aflag = retirement(age, sal, pcs, sg)
            return render_template('retirement.html', message=message)
    return render_template('retirement.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)