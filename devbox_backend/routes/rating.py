from flask import Blueprint
from flask import request
from flask import current_app

from routes.util import GET
from routes.util import POST
from logic.rating import valid_ratings
from logic.exceptions import InvalidUsage, NotFoundError

snacks = [
    "coconut almond butter cliff bar",
    "strawberry fig bar",
    "lemonzest luna bar",
    "chocolate peanut butter luna bar",
    "peanut butter dark chocolate healthy grains kind bar",
    "oat & honey kind healthy grains kind bar",
    "dutch caramel & vanilla rip van wafels",
    "cookies & cream rip van wafels",
    "organic dried mango",
    "dried blenheim apricots",
    "kirkland organic fruit snacks",
    "cinnamon & spice quaker instant oatmeal",
    "maple & brown sugar quaker instant oatmeal",
    "apple & cinnamon quaker instant oatmeal",
    "original quaker instant oatmeal",
    "white cheddar cheez-it",
    "original turkey jerky",
    "black pepper beef jerky",
    "sea salt crunchy chickpeas",
    "creamy peanut butter jif power ups",
    "strawberry jif power ups",
]


blueprint = Blueprint(
    name='rating',
    import_name=__name__,
    url_prefix='/rating',
)

@blueprint.route('/', methods=[GET])
def get_ratings():
    response = {}
    for snack in snacks:
      response[snack] = get_rating(snack)
    return response

@blueprint.route('/<snack>', methods=[GET])
def get_rating(snack):
    redis_client = current_app.extensions.get('redis')
    snack_rating_key = '{}_rating'.format(snack)
    snack_count_key = '{}_count'.format(snack)
    pipe = redis_client.pipeline()
    pipe.get(snack_rating_key)
    pipe.get(snack_count_key)
    rating, count = pipe.execute()
    if rating is None or count is None:
        raise NotFoundError('Invalid snack', status_code=404)
    count = int(count)
    rating = int(rating)
    if count != 0:
      rating = int(rating/count)
    return {
        'rating': rating,
        'count': count
    }

@blueprint.route('/fill', methods=[POST])
def fill_ratings():
    redis_client = current_app.extensions.get('redis')
    for snack in snacks:
        add_rating(snack, 0, 0, redis_client)
    return {'status': 200}


def add_rating(snack, rating, count, redis_client):
    snack_rating_key = '{}_rating'.format(snack)
    snack_count_key = '{}_count'.format(snack)
    pipe = redis_client.pipeline()
    pipe.set(snack_rating_key, rating)
    pipe.set(snack_count_key, count)
    pipe.execute()


@blueprint.route('<snack>', methods=[POST])
def update_rating(snack):
    if int(request.form.get('rating')) not in valid_ratings:
        raise InvalidUsage('Rating value is invalid', status_code=422)

    redis_client = current_app.extensions.get('redis')
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
        'rating': rating,
        'count': count,
    }

    return response
