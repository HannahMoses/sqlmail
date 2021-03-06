from flask import Flask, request,render_template,url_for
from emailer import send_email

app = Flask(__name__)
app.config['DEBUG'] = True#this reloads Flask app everytime I make changes to main.py


@app.route("/india")
def india():
    print("python enabled to print this")
    return render_template("IndiaWorks.html")

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
@app.route("/email",methods=["GET"])
def email():
    return render_template("sqlmailaddList.html")
@app.route("/email",methods=["POST"])
def email_post():
    firstname= request.form["firstname"]
    email = request.form["email"]
    exerhours=request.form["exerhours"]
    print(firstname)
    print(email)
    print(exerhours)
    send_email(email,firstname,exerhours)
    return render_template("sqlmailaddList.html")

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
