from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

@app.route('/api/v1/post', methods=['POST'])
def printPost():
    content_type = request.headers.get('Content-Type')
    try:
        if (content_type == 'application/json'):
            json = request.json
            return json
        else:
            return 'Content-Type not supported!'
    except Exception as e:
        return e 

if __name__ == '__main__':
    app.run()