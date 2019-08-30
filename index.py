from flask import Flask, Response, render_template
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
def homepage(path):
    return render_template("main.html",title='Inicio')
    

@app.route('/<path:path>')
def catch_all(path):
    return Response("<h1>Flask on Now</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")
