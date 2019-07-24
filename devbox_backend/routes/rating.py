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


@blueprint.route('/<snack>', methods=[GET])
def get_rating(snack):
    return {'snack': snack}


@blueprint.route('<snack>', methods=[POST])
def update_rating(snack):
    rating = int(request.args.get('value'))

    if rating not in valid_ratings:
        raise InvalidUsage('Rating value is invalid', status_code=422)

    response = {
        'snack': snack,
        'rating': rating,
    }

    return response
