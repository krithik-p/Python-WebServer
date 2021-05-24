from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    req = request.method
    head = request.headers
    return render_template("page1.html",req=req,head=head)

@app.route('/page2.html', methods=['GET'])
def page2():
    return render_template("page2.html")

@app.route('/page3.html', methods=['GET'])
def page3():
    return render_template("page3.html")

@app.route('/getmoved.html', methods=['GET'])
def moved():
    return redirect("https://www.google.com"),301

#@app.route('/file404', methods=['GET'])
#def notfound():
 #   return ("invalidfile.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0" ,debug=False, port=5050)
