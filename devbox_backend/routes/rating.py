from flask import Blueprint
from flask import request

from routes.util import GET
from routes.util import POST
from logic.rating import valid_ratings
from logic.exceptions import InvalidUsage

blueprint = Blueprint(
    name='rating',
    import_name=__name__,
    url_prefix='/rating',
)

from app import redis_client

@blueprint.route('/<snack>', methods=[GET])
def get_rating(snack):
    snack_rating_key = '{}_rating'.format(snack)
    snack_count_key = '{}_count'.format(snack)
    pipe = redis_client.pipeline()
    pipe.get(snack_rating_key)
    pipe.get(snack_count_key)
    rating, count = pipe.execute()
    response = {
        'rating': int(rating),
        'count': int(count)
    }

    return response

@blueprint.route('<snack>', methods=[POST])
def update_rating(snack):
    rating = int(request.args.get('value'))
    if rating not in valid_ratings:
        raise InvalidUsage('Rating value is invalid', status_code=422)

    snack_rating_key = '{}_rating'.format(snack)
    snack_count_key = '{}_count'.format(snack)

    pipe = redis_client.pipeline()
    pipe.get(snack_rating_key)
    pipe.get(snack_count_key)        
    rating, count = pipe.execute()
    rating = rating or 0
    count = count or 0
    pipe = redis_client.pipeline()
    rating = int(rating) + int(request.form.get('rating'))
    count = int(count) + 1
    pipe.set(snack_rating_key, rating)
    pipe.set(snack_count_key, count)
    pipe.execute()
    
    response = {
        'snack': snack,
        'rating': rating
    }

    return response
