from flask import Flask
from flask import jsonify

import routes
from routes import rating
from logic.exceptions import InvalidUsage

app = Flask(__name__)
app.register_blueprint(routes.blueprint)
app.register_blueprint(rating.blueprint)


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


if __name__ == '__main__':
    app.run()
