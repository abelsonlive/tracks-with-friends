from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')


@app.route('/track', methods=['POST'])
def add_track():
    print request.files['file']
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)