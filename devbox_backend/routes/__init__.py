from flask import Blueprint
from flask import request

blueprint = Blueprint(
    name='',
    import_name=__name__,
)

@blueprint.route('/')
def home():
    return {
        'data': 'success'
    }