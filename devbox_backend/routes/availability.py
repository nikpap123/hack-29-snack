from flask import Blueprint

from routes.util import GET

blueprint = Blueprint(
    name='availability',
    import_name=__name__,
    url_prefix='/availability',
)


@blueprint.route('/', methods=[GET])
def get_availability():

    # TODO replace with response from core logic
    response = {
        'beef jerky': {
            'available': True,
            'level': None,
        },
        'cheez its': {
            'available': False,
            'level': None,
        },
    }

    return response
