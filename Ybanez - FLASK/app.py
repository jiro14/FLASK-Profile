from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/contact')
def contact():
    return render_template('contacts.html')

@app.route('/touppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/areaOfTriangle', methods=['GET', 'POST'])
def areaOfTriangle():
    area = None
    if request.method == 'POST':
        base = float(request.form['base'])
        height = float(request.form['height'])
        area = 0.5 * base * height
    return render_template('areaofTriangle.html', area=area)

@app.route('/areaOfcircle', methods=['GET', 'POST'])
def areaOfcircle():
    area = None
    if request.method == 'POST':
        radius = float(request.form['radius'])
        area = 3.14 * radius ** 2
    return render_template('areaOfcircle.html', area=area)

if __name__ == "__main__":
    app.run(debug=True)
