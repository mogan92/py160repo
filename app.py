from flask import Flask , render_template ,  request

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/result',methods=['POST'])
def display():
    x = request.form['num1']
    y = request.form['num2']
    add = int(x) + int(y)
    sub = int(x) - int(y)
    return render_template('display.html', num1=x, num2=y, add=add, sub=sub)

if __name__ == '__main__':
    app.run(debug=True)