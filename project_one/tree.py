from flask import Flask, render_template , request

app = Flask(__name__)

@app.route("/hello")
def addition():
    a =34
    b= 44
    sum = a+b
    return sum

if __name__ == "__main__":
    app.run()