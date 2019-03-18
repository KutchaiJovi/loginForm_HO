from flask import Flask, render_template, request
#render_template -- jinja2 statements

app = Flask (__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

#@app.route('/hello/<name>')
#def hello_name(name):
#    return "Hello, %s" % name
#http://my-flask-app.com:5000/hello/kutch

@app.route('/hello/<name>')
def hello_name(name):
    return render_template('hello.html', name=name)

@app.route('/login', methods=['GET'])
def login_form():
    return render_template('login_form.html')

@app.route('/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']
    return "Email: %s <br> Password: %s" % (email, password)

# HOMEWORK #
@app.route('/loginForm', methods=['GET'])
def login_form1():
    return render_template('loginForm_HO_Viray.html')

@app.route('/loginForm', methods=['POST'])
def login_user1():

    email1 = request.form['email']
    password1 = request.form['password']

    if email1 == 'test@flask.app' and password1 == 'password123':
        #return render_template('success.html', value=True)
        return render_template('success.html')
    else:
        #return "Try again!"
        return render_template('tryAgain.html')
        #return render_template('success.html', value1=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)