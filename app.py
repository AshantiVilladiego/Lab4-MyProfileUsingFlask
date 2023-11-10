from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/progworks')
def progworks():
    return render_template('progworks.html')

@app.route('/areaOfcirle', methods=['GET', 'POST'])
def areaOfcirle():
    area_result = None
    radius = None
    pi = 3.14159
    if request.method == 'POST':
        try:
            radius = int(request.form.get('radius'))
            area_result = pi * int(radius)**2
        except ValueError:
            pass
    return render_template('areaOfcirle.html', area_result=area_result, radius=radius)

@app.route('/areaOfTriangle', methods=['GET','POST'])
def areaOfTriangle():
    area_result = None
    if request.method == 'POST':
        base_str = request.form.get('base')
        height_str = request.form.get('height')
        try:
            base = int(base_str)
            height = int(height_str)
            area_result = 0.5 * base * height
        except ValueError:
            pass
    return render_template('areaOfTriangle.html', area_result=area_result)

if __name__ == "__main__":
    app.run(debug=True)
