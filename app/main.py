from flask import Flask # import the flask module we installed earlier
import socket
app = Flask(__name__) # Initialise the flask app as app

@app.route('/') # Declare the '/' route for app using a route decorator
def hello_world():
    return f"You did it. Hello World from {socket.gethostname()}"

if __name__ == "__main__":
        app.run(debug=True, host='0.0.0.0')
