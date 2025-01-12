from flask import Flask
from controllers.user_controller import user_controller

app = Flask(__name__)

app.register_blueprint(user_controller)

@app.route('/')
def base():
    return {'Status': 'UP'}

if __name__ == "__main__":
    app.run(port=5000, debug=True)