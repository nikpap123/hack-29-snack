from flask import Blueprint
from flask import request

from routes.util import GET

blueprint = Blueprint(
    name='nutrition',
    import_name=__name__,
    url_prefix='/nutrition',
)


@blueprint.route('/', methods=[GET])
def get_all_nutrition():
    # TODO call core logic to retrieve all nutrition data
    return {}


@blueprint.route('/<snack>', methods=[GET])
def get_nutrition(snack):
    is_image_requested = str(request.args.get('is_image_requested'))
    is_image_requested = True if is_image_requested.lower() == 'true' else False

    if is_image_requested:
        # TODO call core logic for retrieving nutrition image
        pass

    else:
        # TODO call core logic for retrieving individual nutrition
        pass

    return {}
