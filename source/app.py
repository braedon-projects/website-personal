from flask import Flask, render_template, request, redirect, url_for
from driver import bmi, retirement
app = Flask(__name__, template_folder='.')

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        if 'getbmi' in request.form:
            return redirect(url_for('getbmi'))
        if 'retirement' in request.form:
            return redirect(url_for('retire'))
        
    return render_template('index.html')
    # homepage go here
    print('home is where the heart is')

@app.route('/getbmi', methods=['POST', 'GET'])
def getbmi():
    if request.method == 'POST':
        if request.form['submit'] == 'submit':
            height = float(request.form['height'])
            weight = float(request.form['weight'])
            cat, out = bmi(weight, height)
            return render_template('bmi.html', category = cat, message = out)
    return render_template('bmi.html')
    #bmi page go here
    print('bmi')

@app.route('/retirement', methods=['POST', 'GET'])
def retire():
    if request.method == 'POST':
        if request.form['submit'] == 'submit':
            age = float(request.form['age'])
            sal = float(request.form['salary'])
            pcs = float(request.form['percentsaved'])
            sg = float(request.form['savingsgoal'])
            message = retirement(age, sal, pcs, sg)
            return render_template('retirement.html', message=message)
    return render_template('retirement.html')
    #retirment page go here
    print('retirement')

if __name__ == '__main__':
    app.run(debug=True, port=4321)