from Flask import Flask,request,redirect,render_template

app = Flask(__name__)#cretes a Flask app
app.config[DEBUG] = True

tasks = []
@app.route('/todos',methods=['POST','GET'])
def todos():
    if request.method='POST':
        task = request.form['task'
        tasks.append(task)]

    return render_template('todos.hml',title="TODOs",tasks=tasks)

app.run()
