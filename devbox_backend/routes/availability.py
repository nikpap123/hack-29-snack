from flask import Blueprint

from routes.util import GET
from logic.availability import get_latest_availability

blueprint = Blueprint(
    name='availability',
    import_name=__name__,
    url_prefix='/availability',
)


@blueprint.route('/', methods=[GET])
def get_availability():

    # TODO replace with response from core logic
    response = {
        'white cheddar cheez it': {
            'available': True,
            'level': None,
        },
        'sea salt crunchy chickpeas': {
            'available': False,
            'level': None,
        },
    }
    response = get_latest_availability()
    print(len(response))
    return response
