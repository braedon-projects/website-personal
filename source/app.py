from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__, template_folder='.')

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        if 'bmi' in request.form:
            return redirect(url_for('bmi'))
        if 'retirement' in request.form:
            return redirect(url_for('retirement'))
        
    return render_template('index.html')
    # homepage go here
    print('home is where the heart is')

@app.route('/bmi', methods=['POST', 'GET'])
def bmi():
    if request.method == 'POST':
        print('do something')

    return render_template('bmi.html')
    #bmi page go here
    print('bmi')

@app.route('/retirement', methods=['POST', 'GET'])
def retirement():
    if request.method == 'POST':
        print('do something')

    return render_template('retirement.html')
    #retirment page go here
    print('retirement')

if __name__ == '__main__':
    app.run(debug=True, port=4321)