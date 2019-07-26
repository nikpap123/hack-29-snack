import json

from datetime import datetime, timedelta
from flask import Blueprint
from routes.util import GET
from logic.availability import get_latest_availability
from flask import current_app

blueprint = Blueprint(
    name='availability',
    import_name=__name__,
    url_prefix='/availability',
)

IMAGE_TIMESTAMP_KEY = 'image_timestamp'
AVAILABILITY = 'availability'
TIMESTAMP_FORMAT = "%Y/%m/%d:%H-%M-%S"

def should_rerun_model(redis_client):
    timestamp_val = redis_client.get(IMAGE_TIMESTAMP_KEY)
    if timestamp_val is None:
        return True
    timestamp = datetime.strptime(timestamp_val.decode('utf-8'), TIMESTAMP_FORMAT)
    now = datetime.now()
    if now < timestamp + timedelta(minutes=1):
        return False

    return True

@blueprint.route('/', methods=[GET])
def get_availability():
    redis_client = current_app.extensions.get('redis')
    if should_rerun_model(redis_client):
        availability = get_latest_availability()
        if availability:
            availability_str = json.dumps(availability)
            redis_client.set(AVAILABILITY, availability_str)
            redis_client.set(IMAGE_TIMESTAMP_KEY, datetime.now().strftime(TIMESTAMP_FORMAT))
            avail = redis_client.get(AVAILABILITY)
            return availability

    avail = json.loads(redis_client.get(AVAILABILITY))
    return avail
