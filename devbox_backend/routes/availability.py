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
    response = get_latest_availability()
    return response
