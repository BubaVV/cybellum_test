from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/flask')
def hello_world():
    return 'Hello from Flask!\n'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)