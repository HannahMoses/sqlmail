from flask import Flask, request,render_template

app = Flask(__name__)
app.config['DEBUG'] = True#this reloads Flask app everytime I make changes to main.py


@app.route("/india")
def india():
    print("python enabled to print this")
    return render_template("IndiaWorks.html")

@app.route("/exerhours")
def exerhours():
    return render_template("gymtimeaddList.html")
form = """
<!DOCTYPE HTML>
<html>
    <body>
        <form action="/hello" method='post'>
            <label for="myfirstname">My firstname</label>
            <input id="myfirstname" type="text" name="myfirstname" />
            <input type="submit" value="submit name now" />
        </form>
    </body>
</html>

"""
@app.route("/")
def index():
    return form
@app.route("/hello",methods=['POST'])
def hello():
    myfirstname = request.form['myfirstname']
    return '<h1> Hello, ' + myfirstname +'<h1>'
@app.route("/new")
def new():
    return render_template("gymtimeaddList.html")
@app.route("/ipform")
def ipform():
    return render_template("ipform.html")
app.run()




"""# extra space

@app.route("/sendgymail")
def sendgymail():
    myfirstname = request.args.get('myfirstname')
    return ("Browser is sending email")

#extra code to test processing forms rendered by server using flask
@app.route("/test")
def test():
    return render_template("gymtimeaddList.html")
"""
