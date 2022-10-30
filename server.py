from distutils.log import debug
from flask import Flask, request, render_template
from flaskwebgui import FlaskUI
from sqlalchemy import true
# Create the app object

app = Flask(__name__, template_folder='templates')
ui = FlaskUI(app, width=500, height=500)

def basic_calculator(a, b, operator):
    if(a.isnumeric() and b.isnumeric()):
        a = float(a)
        b = float(b)
        if(operator == '+'):
            result = a + b
        elif(operator == '-'):
            result = a - b
        elif (operator == 'x'):
            result = a*b
        elif(operator == '/'):
            if(b == 0): result = "Please enter a valid value."
            else: result = a/b
        elif(operator == 'mod'):
            result = a%b
        elif(operator == "*"):
            result = a**b
        else:
            result = "Please enter a valid value."
    else:
        result = 'Please enter a valid value.'
    return result

# Define calculator
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calc',methods=['POST'])
def calc():

    a = request.form['a']
    b = request.form['b']
    operation = str(request.form['operation'])

    result = basic_calculator(a,b,operation)

    return render_template('index.html', text=str(result))

if __name__ == "__main__":
    ui.run()
    