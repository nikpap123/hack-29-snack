from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask_redis import FlaskRedis

import routes
# from routes import rating
from routes import availability
from routes import nutrition
from logic.exceptions import InvalidUsage

app = Flask(__name__)
redis_client = FlaskRedis(app)
app.register_blueprint(routes.blueprint)
# app.register_blueprint(rating.blueprint)
app.register_blueprint(availability.blueprint)
app.register_blueprint(nutrition.blueprint)
CORS(app)


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


if __name__ == '__main__':
    app.run()
