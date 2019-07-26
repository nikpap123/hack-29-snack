from flask import Blueprint, current_app, request
from routes.util import GET, POST

blueprint = Blueprint(
    name='review',
    import_name=__name__,
    url_prefix='/review',
)


@blueprint.route('/<snack>', methods=[GET])
def get_review(snack):
    redis_client = current_app.extensions.get('redis')
    snack_reviews_key = '{}_reviews'.format(snack)
    num_snacks = redis_client.llen(snack_reviews_key)
    reviews = redis_client.lrange(snack_reviews_key, 0, num_snacks)
    return {'reviews': [review.decode('utf-8') for review in reviews]}


@blueprint.route('/<snack>', methods=[POST])
def post_review(snack):
    review_text = request.form.get('review')

    redis_client = current_app.extensions.get('redis')
    snack_reviews_key = '{}_reviews'.format(snack)
    redis_client.lpush(snack_reviews_key, review_text)
    return 'success'
